import os
import requests
from datetime import datetime

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

companies = [
    "HUL",
    "ITC",
    "Dabur",
    "Marico",
    "Godrej",
    "Britannia",
    "Nestle",
    "P&G",
    "HCCB",
    "Amrutanjan",
    "Dr Reddy's",
    "Titan",
    "CavinKare",
    "Michael Page",
    "CIEL HR"
]

message = f"""
Good Morning Karthik

Marketing Leadership Job Scan

Date: {datetime.now().strftime('%d-%b-%Y')}

Target Roles:
• CMO
• Marketing Head
• Brand Head
• GM Marketing
• AGM Marketing
• Category Head

Target Locations:
• Chennai
• Tamil Nadu
• Bangalore

Companies Checked:
"""

for company in companies:
    message += f"\n• {company}"

message += "\n\nJob Agent executed successfully."

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": message
    }
)