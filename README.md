# Week 8: Local LLM Inference Using Ollama

## Project Overview
This project demonstrates how to run a Large Language Model (LLM) locally using Ollama and the Gemma 3 (1B) model. It processes prompts from different domains and stores the generated responses for analysis.

## Objectives
- Run a local LLM using Ollama.
- Generate responses for prompts from different domains.
- Measure response time and response word count.
- Store results in CSV and text files.
- Analyze model responses using a Jupyter Notebook.

## Technologies Used
- Python
- Ollama
- Gemma 3 (1B)
- Pandas
- Jupyter Notebook

## Project Structure
```text
Local_LLM_Inference/
├── dataset/
│   ├── prompts.csv
│   ├── llm_responses.csv
│   ├── response_comparison.csv
│   └── conversation_history.txt
├── notebook/
│   └── Week8_Local_LLM_Inference.ipynb
├── local_llm.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run
1. Install Ollama.
2. Download the model using `ollama pull gemma3:1b`.
3. Install the required Python packages using `pip install -r requirements.txt`.
4. Run the program using `python local_llm.py`.
5. Open the Jupyter Notebook to explore the prompts, responses, and performance statistics.

## Output Files
- `llm_responses.csv`: Stores prompts and generated responses.
- `response_comparison.csv`: Contains response word counts and response times.
- `conversation_history.txt`: Stores the conversation history for each prompt.

## Conclusion
This project demonstrates local LLM inference using Ollama and Gemma 3 (1B). It generates responses to prompts across different domains and records basic performance statistics for analysis.