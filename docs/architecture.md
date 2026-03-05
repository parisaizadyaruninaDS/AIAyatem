
# System Architecture: TechNova RAG Bot

## 1. High-Level Overview
The system follows a modular architecture to satisfy both **Innovation (INN)** and **Research (RES)** requirements.


## 2. System Elements
* **Input Layer:** Captures user text and performs **Sentiment Analysis** to determine if the user is frustrated.
* **Retrieval Layer (RAG):** Searches the `data/technova_product_manual.pdf` for the most relevant technical facts.
* **Privacy Guardrail:** A middleware that scans the retrieved data and user query for PII (emails, names) and masks them.
* **Generation Layer:** Uses an LLM (e.g., GPT-4o-mini or Llama 3) to synthesize a final answer based *only* on the retrieved facts.

## 3. Data Flow
1. **User Query** -> 2. **Sentiment Check** -> 3. **Knowledge Retrieval** -> 4. **Privacy Scrubbing** -> 5. **Final Response Generation**.
