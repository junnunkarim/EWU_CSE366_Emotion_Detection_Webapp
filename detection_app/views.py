from django.shortcuts import render

import ollama

# from .forms import PromptForm
from .models import PromptModel


# ------------------------------------------------ #
# --------------- helper functions --------------- #
# ------------------------------------------------ #
def get_answer_from_model(prompt: str):
    """
    Prompt the model and get the answer as output.
    """

    response = ollama.chat(
        model="emotion_analysis_mistral_0.2_7b:latest",
        messages=[
            {
                "role": "user",
                "content": f"[INST]Analyze the emotion of the text and determine if it is Happy, Love, Sadness, Anger or Fear, and return the answer as the corresponding emotion label 'Happy' or 'Love' or 'Sadness' or 'Anger' or 'Fear'.[/INST]\n### Text: {prompt}\n### Emotion:",
            },
        ],
    )

    return response["message"]["content"]


def get_history():
    """
    Get the history of all prompts with replies.
    """

    return PromptModel.objects.all()


# ------------------------------------- #
# --------------- views --------------- #
# ------------------------------------- #
def home(request):
    # create a dictionary to send data for rendering in the template
    context = {}
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
