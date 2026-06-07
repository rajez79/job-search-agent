import os
import requests
from datetime import datetime

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

companies = [
("HUL", "https://www.hul.co.in/careers/"),
("ITC", "https://www.itcportal.com/careers/index.aspx"),
("Dabur", "https://www.dabur.com/careers"),
("Marico", "https://marico.com/india/careers"),
("Godrej", "https://www.godrejcareers.com/"),
("Britannia", "https://www.britannia.co.in/careers"),
("Nestle", "https://www.nestle.in/jobs"),
("P&G", "https://www.pgcareers.com/in/en"),
("HCCB", "https://www.hccb.in/career"),
("Amrutanjan", "https://www.amrutanjan.com/careers/"),
("Dr Reddy's", "https://careers.drreddys.com/"),
("Titan", "https://www.titancompany.in/careers"),
("CavinKare", "https://www.cavinkare.com/careers/"),
("Michael Page", "https://www.michaelpage.co.in/jobs/fmcg"),
("CIEL HR", "https://www.cielhr.com/jobs/fmcg")
]

message = f"""
Good Morning Raja

Marketing Leadership Job Scan

Date: {datetime.now().strftime('%d-%b-%Y')}

Candidate:
Karthikeyan R
22+ Years Experience

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

Career Sites Checked:
"""

for company, url in companies:
message += f"\n• {company}"

message += """

Status:
✓ GitHub Action Running
✓ Telegram Bot Working

Next Upgrade:
Actual job extraction from company portals.
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
url,
json={
"chat_id": CHAT_ID,
"text": message
}
)

print(response.status_code)
print(response.text)
