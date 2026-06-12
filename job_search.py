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

unique_jobs = []
seen_urls = set()

for job in jobs:

    if job["url"] not in seen_urls:

        seen_urls.add(
            job["url"]
        )

        unique_jobs.append(
            job
        )