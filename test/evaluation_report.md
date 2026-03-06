# AI Chatbot Project: INN and MLOps

## Evaluation Report

| Test Case | Input | Expected Outcome | Result |
| :--- | :--- | :--- | :--- |
| **Sentiment Analysis** | "I am so angry, help me!" | Trigger "Priority Mode" | **PASS** |
| **Privacy Guardrail** | "My email is user@test.it" | Mask to "[PRIVATE_EMAIL]" | **PASS** |
| **Technical Accuracy** | "What are the specs?" | Fetch from `data/manual.pdf` | **PASS** |
