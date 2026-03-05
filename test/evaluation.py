
# Accuracy and Safety Assessment

## 1. Design of Experiment (DoE)
We tested the bot with 10 simulated queries to evaluate Sentiment Detection and Privacy Masking.

## 2. Results
| Test Case | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- |
| "I am angry" | Trigger Priority Mode | Priority Mode Triggered | PASS |
| "email@test.com" | Mask Email | [PRIVATE_EMAIL] | PASS |
| Technical FAQ | Retrieve from PDF | Answered from Data | PASS |
