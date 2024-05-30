from django.shortcuts import render

from ollama import generate

# from .forms import PromptForm
from .models import PromptModel


# ------------------------------------------------ #
# --------------- helper functions --------------- #
# ------------------------------------------------ #
def get_answer_from_model(text: str):
    """
    Prompt the model and get the answer as output.
    """
    # for gemma
    prompt = f"""Analyze the emotion of the text enclosed in square brackets,
determine if it is Happy, Love, Sadness, Anger or Fear, and return the answer only as
the corresponding sentiment label 'Happy' or 'Love' or 'Sadness' or 'Anger' or 'Fear'

[{text}] = """.strip()

    response = generate(
        model="emotion_analysis_gemma_2b_v3.3.0",
        prompt=prompt,
        # response will be recieved in a single reply
        stream=False,
        options={
            # max new token count
            "num_predict": 2,
            # controls creativity when generating
            # temperature = 0 means the response is reproducible
            "temperature": 0,
        },
    )

    return response["response"]


def get_history():
    """
    Get the history of all prompts with response.
    """
    return PromptModel.objects.all()


# ------------------------------------- #
# --------------- views --------------- #
# ------------------------------------- #
def home(request):
    # create a dictionary to send data for rendering in the template
    context = {}
    # get history of all prompts with response from database
    history = get_history()

    if request.method == "POST":
        # get prompt from user
        prompt = request.POST["prompt"]
        # generate response for the user prompt
        answer = get_answer_from_model(prompt)

        # store the user prompt along with the response in the database
        prompt_answer = PromptModel(prompt=prompt, answer=answer)
        prompt_answer.save()

    # insert history inside dictionary to send it to the template
    context["history"] = history

    return render(request, "detection_app/home.html", context)
