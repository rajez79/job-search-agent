import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from config import TARGET_ROLES, JOB_SOURCES

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

print("Karthikeyan Job Agent Started")

jobs = []

for site in JOB_SOURCES:

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

            title = link.get_text(
                " ",
                strip=True
            )

            href = link["href"]

            if not title:
                continue

            title_lower = title.lower()

            if any(
                role.lower() in title_lower
                for role in TARGET_ROLES
            ):

                if not href.startswith("http"):
                    href = requests.compat.urljoin(
                        site,
                        href
                    )

                jobs.append({
                    "title": title,
                    "url": href
                })

    except Exception as e:
        print(
            f"Error scanning {site}: {str(e)}"
        )

message = (
    f"Daily Marketing Leadership Job Scan\n\n"
    f"Candidate: Karthikeyan R\n"
    f"Date: {datetime.now().strftime('%d-%b-%Y')}\n"
    f"Jobs Found: {len(jobs)}\n\n"
)

for idx, job in enumerate(jobs[:20], start=1):

    message += (
        f"{idx}. {job['title']}\n"
        f"{job['url']}\n\n"
    )

telegram_url = (
    f"https://api.telegram.org/bot{TOKEN}/sendMessage"
)

requests.post(
    telegram_url,
    json={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)
