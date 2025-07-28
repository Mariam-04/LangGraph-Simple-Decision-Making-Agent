# Intern-Gpt-Rag

A mini Retrieval-Augmented Generation (RAG) chatbot to answer internship-related queries using LangChain, LangGraph, and ChromaDB.

## Setup

1. Clone the repo:
   git clone https://github.com/your-username/InternGPT.git
   cd InternGPT

## Install dependencies:

pip install -r requirements.txt
Set your OpenAI API key:

export OPENAI_API_KEY=your_openai_key
Run the app:

python app.py

## Project Files
app.py — LangGraph pipeline with query rewrite → retrieval → prompt

retriever_setup.py — Loads a basic internship FAQ and stores vectors in ChromaDB

prompt_templates.py — Custom RAG prompt format

docs/internship_faq.txt — Demo data for the retriever

## Example Questions
“Do 2nd year students qualify for this internship?”

“Is it a paid internship?”

“How long does the program last?”
