from django.shortcuts import render

import ollama

from .forms import PromptForm
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
    return PromptModel.objects.all()


# ------------------------------------- #
# --------------- views --------------- #
# ------------------------------------- #
def home(request):
    context = {}
    history = get_history()

    if request.method == "POST":
        prompt = request.POST["prompt"]
        answer = get_answer_from_model(prompt)

        prompt_answer = PromptModel(prompt=prompt, answer=answer)
        prompt_answer.save()

    context["history"] = history

    return render(request, "detection_app/home.html", context)
