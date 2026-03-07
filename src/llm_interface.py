import re

def generate_response(user_input, sentiment):
    # RES Requirement: Privacy Masking
    email_pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    safe_input = re.sub(email_pattern, "[MASKED_PII]", user_input)

    # Logic for Sentiment-Aware Routing (INN)
    if sentiment == "ANGRY":
        answer = "I've prioritized your request due to the urgency. Checking the manual now..."
        confidence = "High (Priority Mode)"
    else:
        answer = "Searching the TechNova knowledge base for your answer..."
        confidence = "Medium"
    
    return answer, confidence, safe_input
