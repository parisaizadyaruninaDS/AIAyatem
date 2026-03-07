import csv
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def log_interaction(user_input, answer, confidence, sentiment):
    # Innovation: Monitoring for "Drift" or high-frustration cases
    if sentiment == "ANGRY":
        logger.warning(f"HIGH ALERT: Frustrated user detected. Query: {user_input[:30]}")
    
    with open("data/logs.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, answer, confidence, sentiment])
