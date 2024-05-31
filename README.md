# Bangla Emotion Detection with LLM

A project about fine-tuning LLMs to detect emotion in Bangla E-Commerce reviews

- University: East West University
- Course: CSE366 (Artificial Intelligence)

# Directory Structure

<details>
<summary><b>click here</b></summary>

```
EWU_CSE366_Emotion_Detection_Webapp
├── README.md
├── datasets
│   └── bangla_sentiment_and_emotion_analysis.csv
├── django_src
│   ├── db.sqlite3
│   ├── detection_app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── static
│   │   ├── templates
│   │   │   └── detection_app
│   │   │       ├── base.html
│   │   │       └── home.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── emotion_detection
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── docs
│   ├── cse366_project_details.pdf
│   ├── cse366_project_report__group_10.pdf
│   └── cse366_project_report_and_viva_guidelines.md
├── models
│   └── ollama_modelfile
├── notebooks
│   ├── finetune_gemma_2b_bangla_emotion_analysis__v1.1.0.ipynb
│   ├── finetune_gemma_2b_bangla_emotion_analysis__v3.3.1.ipynb
│   ├── finetune_gemma_2b_bangla_emotion_analysis__v3.4.0.ipynb
│   ├── finetune_gemma_2b_bangla_emotion_analysis__v3.4.1.ipynb
│   └── finetune_mistral_0.2_7b_bangla_emotion_analysis__v0.1.0.ipynb
├── requirements.txt
└── ss
    └── bangla_emotion_analysis.png
```

</details>

# Setup
> [!WARNING]  
> This setup assumes that you are using a Linux distribution.

<details>
<summary><b>click here</b></summary>

## Clone and Installation
- Install `python` using your package manager
- Install `ollama` following instructions from the official repo: [Ollama Github](https://github.com/ollama/ollama)
- Create a virtual environment in your preferred directory

    ```bash
    python -m venv bangla_emotion_llm
    ```

- Activate the virtual environment

    ```bash
    source bangla_emotion_llm
    ```

- Update `pip`

    ```bash
    python -m pip install --upgrade pip
    ```

- Clone this repo to your preferred directory

    ```bash
    git clone https://github.com/junnunkarim/EWU_CSE366_Emotion_Detection_Webapp
    ```

- Change current directory to the cloned directory

    ```bash
    cd EWU_CSE366_Emotion_Detection_Webapp
    ```

- Install necessary python libraries from the `requirements.txt`

    ```bash
    pip install -r requirements.txt
    ```

## Model Installation
- Download the model from this link - [emotion_analysis_gemma_2b__v3.4.0.gguf](https://drive.google.com/file/d/193nEIq3VgGzBaAgcFnTsOAmHvi7AW6gU/view)
- Move the downloaded model to the `models` directory
- Change directory to `models`

    ```bash
    cd models/
    ```

- Import the model using `ollama`

    ```bash
    ollama create "emotion_analysis_gemma_2b__v3.4.0" -f ollama_modelfile
    ```

- Change directory back to root of the cloned repo

    ```bash
    cd ../
    ```

## Start Server
- Open another terminal and start `ollama` server

    ```bash
    ollama serve
    ```

- In the original terminal, change directory to `django_src`

    ```bash
    cd django_src/
    ```

-  Start the django server

    ```bash
    python manage.py runserver
    ```

- Now you can visit the url `http://127.0.0.1:8000/` to see the test the fine-tuned LLM

</details>

# ScreenShots
![img](/ss/bangla_emotion_analysis.png)

# Credit
- Dataset: [A comprehensive dataset for sentiment and emotion classification from Bangladesh e-commerce reviews](https://www.sciencedirect.com/science/article/pii/S235234092400026X)

# Contributors
- [Junnun Mohamed Karim](https://www.github.com/junnunkarim)
- [Md Murad Khan Limon](https://github.com/muradkhanlimon)
- [Md. Yousuf Hozaifa](https://www.github.com/Yousuf-Hozaifa)
