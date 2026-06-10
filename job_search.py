import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

CAREER_SITES = [
"https://www.hul.co.in/careers/",
"https://www.itcportal.com/careers/index.aspx",
"https://www.dabur.com/careers",
"https://marico.com/india/careers",
"https://www.godrejcareers.com/",
"https://www.britannia.co.in/careers",
"https://www.nestle.in/jobs",
"https://www.pgcareers.com/in/en",
"https://www.hccb.in/career",
"https://www.amrutanjan.com/careers/",
"https://careers.drreddys.com/",
"https://www.titancompany.in/careers",
"https://www.cavinkare.com/careers/",
"https://www.michaelpage.co.in/jobs/fmcg",
"https://www.cielhr.com/jobs/fmcg"
]

KEYWORDS = [
"marketing",
"brand",
"cmo",
"category",
"director",
"head",
"lead",
"marketing-manager",
"marketing-head",
"brand-manager",
"head-of-marketing"
]

HEADERS = {
"User-Agent": "Mozilla/5.0"
}

print("Karthikeyan Job Agent Started")

jobs = set()

for site in CAREER_SITES:

    try:
        print(f"Scanning: {site}")

    response = requests.get(
        site,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for link in soup.find_all("a", href=True):

        href = link["href"]
        href_lower = href.lower()

        if any(
            keyword in href_lower
            for keyword in KEYWORDS
        ):

            if href.startswith("http"):
                jobs.add(href)
            else:
                jobs.add(
                    requests.compat.urljoin(
                        site,
                        href
                    )
                )

except Exception as e:
    print(f"Error scanning {site}: {e}")
```

message = (
f"Daily Marketing Leadership Job Scan\n\n"
f"Candidate: Karthikeyan R\n"
f"Date: {datetime.now().strftime('%d-%b-%Y')}\n"
f"Jobs Found: {len(jobs)}\n\n"
)

if len(jobs) == 0:
message += "No matching jobs found today.\n"

for idx, job in enumerate(sorted(jobs)[:15], start=1):
message += f"{idx}. {job}\n\n"

print(f"Jobs found: {len(jobs)}")
print("Sending Telegram message...")

telegram_url = (
f"https://api.telegram.org/bot{TOKEN}/sendMessage"
)

response = requests.post(
telegram_url,
json={
"chat_id": CHAT_ID,
"text": message[:4000]
},
timeout=30
)

print("Telegram Status:", response.status_code)
print(response.text)

response.raise_for_status()
