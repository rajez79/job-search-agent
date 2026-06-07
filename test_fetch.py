import requests
from bs4 import BeautifulSoup

URL = "https://www.michaelpage.co.in/jobs/fmcg"

KEYWORDS = [
    "marketing",
    "brand",
    "cmo",
    "category",
    "director",
    "head",
    "lead"
]

html = requests.get(URL, timeout=20).text

soup = BeautifulSoup(html, "html.parser")

jobs = set()

for link in soup.find_all("a"):
    href = link.get("href")

    if not href:
        continue

    href_lower = href.lower()

    if "/job-detail/" in href_lower:
        for keyword in KEYWORDS:
            if keyword in href_lower:
                full_url = "https://www.michaelpage.co.in" + href
                jobs.add(full_url)
                break

print("\nMatching Jobs Found:\n")

for job in sorted(jobs):
    print(job)