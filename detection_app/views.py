from django.shortcuts import render

import ollama

# Create your views here.


def get_answer_from_model(prompt: str):
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


def home(request):
    if request.method != "GET":
        prompt = request.POST.get("prompt")
        answer = get_answer_from_model(prompt)

        parcel = {"prompt": prompt, "answer": answer}

        return render(request, "detection_app/home.html", parcel)

    return render(request, "detection_app/home.html")
