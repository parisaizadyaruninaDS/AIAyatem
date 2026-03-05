
import re

# 1. Simple Sentiment Analyzer (Innovation - INN)
def analyze_sentiment(user_input):
    angry_words = ['angry', 'bad', 'broken', 'hate', 'stupid', 'worst', 'help']
    if any(word in user_input.lower() for word in angry_words):
        return "ANGRY"
    return "NEUTRAL"

# 2. Privacy Guardrail (Research - RES / Trustworthiness)
def mask_pii(text):
    # This regex finds email addresses and masks them
    email_pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    return re.sub(email_pattern, "[PRIVATE_EMAIL]", text)

# 3. The Main Bot Logic (Prototype Development)
def technova_bot(user_query):
    # Step A: Check Privacy
    safe_query = mask_pii(user_query)
    
    # Step B: Check Sentiment
    sentiment = analyze_sentiment(safe_query)
    
    # Step C: Generate Response
    if sentiment == "ANGRY":
        response = "🚨 [PRIORITY MODE] I can see you're frustrated. I am looking at the TechNova manual right now to find a solution for you immediately."
    else:
        response = "I am checking the TechNova technical manual for your answer..."
    
    # In a real system, this is where RAG (Retrieval) would happen
    # For the demo, we show we've processed the inputs correctly
    return f"Bot Response: {response} (Processed query: {safe_query})"

# --- Test the system ---
if __name__ == "__main__":
    print(technova_bot("My laptop is broken and I hate this service! my email is test@me.com"))
