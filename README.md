# AIsystem
AI systemPrjChatbot
To ensure reproducibility, this project is containerized using Docker.
1. Build the image: `docker build -t technova-bot .`
2. Run the bot: `docker run technova-bot.`
   Technical Report: TechNova Sentiment-Aware RAG Assistant
Artificial Intelligence Systems

Prof. Roberto Pietrantuono


Parisa Izadiyar


Repository: https://github.com/parisaizadyaruninaDS/AIAyatem



Exam Date: March 13, 2026











1. Introduction and Objectives
In the current landscape of automated customer service, two primary challenges persist: the lack of emotional intelligence in interactions and the technical unreliability (hallucinations) of Large Language Models (LLMs). This project introduces the TechNova RAG Bot, a system designed to address these gaps through a dual-track approach:
•	Innovation (INN): Implementation of a real-time Sentiment-Aware Controller to detect user frustration and trigger high-priority response protocols.
•	Research (RES): Development of a Retrieval-Augmented Generation (RAG) architecture paired with a custom Privacy Guardrail to ensure technical accuracy and data safety.

2. System Engineering Framework: The V-Model
To ensure high-quality software delivery and "rigor and soundness," the project follows the System Engineering V-Model:
2.1 Requirements and Design (Left Side)
•	Stakeholder Needs: We identified TechNova Electronics' need to reduce support ticket volume while maintaining high customer satisfaction.
•	Modular Architecture: The system was decomposed into four functional layers: Input (Sentiment), Retrieval (RAG), Privacy Middleware, and Generation.
2.2 Implementation and Verification (Bottom & Right Side)
•	Development: Core logic was implemented in a modular Python environment (src/app.py), ensuring code maintainability.
•	Testing: We conducted a formal Design of Experiment (DoE) with 10 simulated test cases to verify both the sentiment triggers and privacy masking logic.

3. Innovation Track: Emotional Intelligence
Standard bots often alienate angry customers by providing generic answers. My solution solves this by:
•	Keyword-Based Sentiment Analysis: The bot scans inputs for frustration markers like "angry," "broken," or "bad".
•	Dynamic Response Protocol: If frustration is detected, the system overrides standard responses with a [PRIORITY MODE] flag, informing the user that their issue is being escalated for immediate technical review.
4. Research Track: Trustworthiness & Privacy
To solve the scientific problem of LLM hallucinations and the risk of Personally Identifiable Information (PII) leakage:
•	RAG Implementation: The system restricts the LLM's knowledge base to the technova_product_manual.pdf, ensuring responses are grounded in verified technical facts.
•	Privacy Guardrail Layer: Before any data reaches the core processing engine, a regex-based middleware masks sensitive information. For example, a user inputting an email address will see it masked to [PRIVATE_EMAIL] in the system logs.

5. MLOps and Deployment Lifecycle
The project demonstrates full MLOps maturity through three pillars:
•	Containerization: A Dockerfile is provided in the root directory, allowing the professor to build and run the entire environment with a single command, ensuring full reproducibility.
•	Continuous Monitoring: Every interaction—including sentiment scores and confidence levels—is logged to data/logs.csv for auditability.
•	Traceability: Documentation in the docs/ folder provides a clear link between the initial requirements and the final system architecture.

6. Experimental Validation
Our testing phase proved the system is functional and safe:

Metric	Test Case	Observed Behavior	Result
Sentiment	"I am so angry!"	Triggered [PRIORITY MODE]	PASS
Privacy	"email is test@me.com"	Masked to [PRIVATE_EMAIL]	PASS
Accuracy	Tech Query	Retrieved from manual PDF	PASS

I am so angry
 

email is test@me.com
 

Tech Query
 

7. Conclusion
The TechNova RAG Bot successfully meets the criteria for both Innovation and Research-driven tracks. By applying the V-Model and MLOps principles, we have created a solution that is not just a script, but a reliable, safe, and empathetic system ready for real-world deployment.
 
































