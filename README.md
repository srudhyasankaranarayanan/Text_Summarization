# Text Summarization Using Hugging Face Pipelines

## Project Overview

The **Text Summarization App** is a web application built using Python, Hugging Face Transformers, and Streamlit. It summarizes long paragraphs and articles into shorter, meaningful summaries while preserving the main ideas.

The application uses a pretrained Hugging Face language model to generate summaries from user-provided text.

## Demo Link

https://textsummarization-2sy26g4br3ua4uyw2tmvey.streamlit.app/

## Objectives

- Summarize long text into shorter content.
- Preserve the important information and main ideas.
- Provide a simple and user-friendly interface.
- Learn how to use Hugging Face Pipelines with Streamlit.
- Generate and download summaries easily.

## Technologies Used

- **Python** – Programming language
- **Hugging Face Transformers** – Access to pretrained models and pipelines
- **Streamlit** – Web application interface
- **PyTorch** – Model execution framework

## Features

- Enter or paste long text.
- Generate summaries using a pretrained model.
- Choose short, medium, or long summary lengths.
- Display the generated summary.
- Download the summary as a text file.
- Simple and interactive user interface.

## Project Structure

```text
HF_Summarization/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/srudhyasankaranarayanan/Hugging-Face-Pipelines
cd Hugging_face pipeline
```

If you have not uploaded the project to GitHub, open the project folder directly in VS Code.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Requirements

Create a `requirements.txt` file containing:

```text
streamlit
transformers
torch
```

## Run the Application

Run the following command in the VS Code terminal:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can access the application.

The first run may take longer because the pretrained model needs to be downloaded.

## How It Works

1. The user enters or pastes a paragraph or article.
2. The user selects the desired summary length.
3. The application passes the text to the Hugging Face model.
4. The model generates a concise summary.
5. The summary appears on the screen.
6. The user can download the generated summary.

## Hugging Face Model

The application uses the pretrained model:

`HuggingFaceTB/SmolLM2-360M-Instruct`

This is an instruction-tuned language model used with the `text-generation` pipeline to generate summaries.

## Screenshots

<img width="782" height="562" alt="image" src="https://github.com/user-attachments/assets/48a4b1bb-ea4a-4d24-8b99-d6742b419375" />
<img width="758" height="307" alt="image" src="https://github.com/user-attachments/assets/08ff7926-8332-46c0-80b0-73159feee87d" />
<img width="760" height="385" alt="image" src="https://github.com/user-attachments/assets/adc96eb1-125b-4c34-b00d-ac1ff3310f8a" />
<img width="761" height="385" alt="image" src="https://github.com/user-attachments/assets/42871ff2-6cab-439d-804e-8b49ce32a668" />

## Applications

- Summarizing news articles
- Creating study notes
- Summarizing educational materials
- Condensing reports and documents
- Extracting the main ideas from lengthy text

## Limitations

- Summary quality depends on the input text and the model.
- Important details may occasionally be omitted.
- The first run requires an internet connection to download the model.
- Large inputs may require additional memory and processing time.
- Generated summaries should be checked for accuracy.

## Future Improvements

- Support uploading PDF and TXT files.
- Add multilingual summarization.
- Allow users to compare different models.
- Add summary length and language controls.
- Deploy the application online.

## Conclusion

The Text Summarization App demonstrates how Hugging Face Transformers and Streamlit can be combined to build an AI-powered text summarization application. It provides a practical introduction to pretrained language models, NLP pipelines, and interactive AI applications.

---

## Author

**Srudhya Sankaranarayanan**
