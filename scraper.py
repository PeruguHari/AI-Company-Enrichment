import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


def scrape_page(url, headers):

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        html = response.text

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        for tag in soup(
            [
                "script",
                "style",
                "nav",
                "footer"
            ]
        ):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        emails = list(
            set(
                re.findall(
                    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
                    html
                )
            )
        )

        phones = list(
            set(
                re.findall(
                    r"(?:\+91[- ]?)?[6-9]\d{9}",
                    html
                )
            )
        )

        return {
            "text": text,
            "emails": emails,
            "phones": phones,
            "html": html,
            "soup": soup
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "text": "",
            "emails": [],
            "phones": [],
            "html": "",
            "soup": None
        }


def scrape_website(url):

    print("=" * 50)
    print("VISITING:", url)
    print("=" * 50)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    all_text = ""
    all_emails = set()
    all_phones = set()

    home = scrape_page(
        url,
        headers
    )

    all_text += home["text"][:2000] + " "

    all_emails.update(
        home["emails"]
    )

    all_phones.update(
        home["phones"]
    )

    if home["soup"]:

        keywords = [
            "about",
            "contact",
            "service",
            "services",
            "solution",
            "solutions"
        ]

        links_to_visit = []

        for link in home["soup"].find_all("a"):

            href = link.get("href")

            if not href:
                continue

            href_lower = href.lower()

            if any(
                keyword in href_lower
                for keyword in keywords
            ):

                full_url = urljoin(
                    url,
                    href
                )

                links_to_visit.append(
                    full_url
                )

        links_to_visit = list(
            set(links_to_visit)
        )[:5]

        print("LINKS FOUND:")
        print(links_to_visit)

        for page_url in links_to_visit:

            page = scrape_page(
                page_url,
                headers
            )

            all_text += page["text"][:2000] + " "

            all_emails.update(
                page["emails"]
            )

            all_phones.update(
                page["phones"]
            )

    print("EMAILS:", list(all_emails))
    print("PHONES:", list(all_phones))
    print("TEXT LENGTH:", len(all_text))

    return {
        "text": all_text[:8000],
        "emails": list(all_emails),
        "phones": list(all_phones)
    }