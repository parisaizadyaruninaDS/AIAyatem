# Requirements Analysis: TechNova Customer Assistant

## 1. Stakeholder Needs (INN)
The primary stakeholder is **TechNova Electronics**, a fictional global hardware provider. 
* **Business Need**: Reduce high support ticket volume by automating technical troubleshooting.
* **Innovation**: Standard bots often frustrate users. Our solution integrates **Real-time Sentiment Analysis** to detect user anger and trigger "Conciliatory Response Protocols" or direct human escalation.
* **Functional Requirement**: The bot must retrieve technical specs directly from provided product manuals (PDFs) to ensure accuracy.

## 2. Scientific Problem Statement (RES)
* **The Problem**: Current LLM-based chatbots suffer from **hallucinations** (providing fake technical specs) and **PII (Personally Identifiable Information) leakage**.
* **Limitation of Existing Solutions**: Basic fine-tuning does not prevent a model from "making up" information if it is not in its training data.
* **Research Goal**: Evaluate if a **Retrieval-Augmented Generation (RAG)** architecture significantly reduces hallucination rates compared to a standalone LLM when handling complex technical documentation.

## 3. Evaluation Metrics (Correctness)
To satisfy the project's rigor, we will measure:
* **Faithfulness**: How accurately the bot sticks to the PDF data.
* **Privacy Safety**: The bot's ability to mask sensitive data (emails/phone numbers) using a custom guardrail layer.
