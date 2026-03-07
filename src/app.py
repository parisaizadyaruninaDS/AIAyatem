
import re

def analyze_sentiment(user_input):
    angry_words = ['angry', 'bad', 'broken', 'hate', 'stupid', 'worst', 'help']
    if any(word in user_input.lower() for word in angry_words):
        return "ANGRY"
    return "NEUTRAL"


def mask_pii(text):
    email_pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    return re.sub(email_pattern, "[PRIVATE_EMAIL]", text)

def technova_bot(user_query):
    safe_query = mask_pii(user_query)
    
    sentiment = analyze_sentiment(safe_query)
    
    if sentiment == "ANGRY":
        response = "🚨 [PRIORITY MODE] I can see you're frustrated. I am looking at the TechNova manual right now to find a solution for you immediately."
    else:
        response = "I am checking the TechNova technical manual for your answer..."
  
    return f"Bot Response: {response} (Processed query: {safe_query})"

if __name__ == "__main__":
    print(technova_bot("My laptop is broken and I hate this service! my email is test@me.com"))





import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def analyze_sentiment(user_input):
    angry_words = ['angry', 'bad', 'broken', 'hate', 'stupid', 'worst', 'help']
    sentiment = "ANGRY" if any(word in user_input.lower() for word in angry_words) else "NEUTRAL"
    logger.info(f"Sentiment Detected: {sentiment} for input: {user_input[:20]}...")
    return sentiment

def mask_pii(text):
    email_pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}'
    masked_text = re.sub(email_pattern, "[PRIVATE_EMAIL]", text)
    if "[PRIVATE_EMAIL]" in masked_text:
        logger.warning("Privacy Alert: PII was detected and masked.")
    return masked_text

def technova_bot(user_query):
    logger.info("New query received.")
    safe_query = mask_pii(user_query)
    sentiment = analyze_sentiment(safe_query)
    
    if sentiment == "ANGRY":
        response = "🚨 [PRIORITY MODE] We are prioritizing your technical issue."
    else:
        response = "I am checking the TechNova technical manual..."
        
    return f"Response: {response}"


if __name__ == "__main__":
    print("--- TechNova Support Bot Active ---")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        print(technova_bot(user_input))
