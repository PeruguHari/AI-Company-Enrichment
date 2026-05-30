import json

from scraper import scrape_website
from ai_processor import generate_insights


def enrich_company(url):

    print("\n" + "=" * 50)
    print("PROCESSING URL:", url)
    print("=" * 50)

    # Step 1: Scrape Website
    scraped = scrape_website(url)

    print("\nSCRAPED TEXT LENGTH:")
    print(len(scraped["text"]))

    print("\nEMAILS FOUND:")
    print(scraped["emails"])

    print("\nPHONES FOUND:")
    print(scraped["phones"])

    print("\nSCRAPED TEXT PREVIEW:")
    print(scraped["text"][:1000])

    # Step 2: Generate AI Insights
    ai_response = generate_insights(
        scraped["text"]
    )

    print("\nAI RESPONSE:")
    print(ai_response)

    # Step 3: Convert AI Response to JSON
    try:

        ai_data = json.loads(
            ai_response
        )

        print("\nJSON PARSE SUCCESS")

    except Exception as e:

        print("\nJSON PARSE FAILED")
        print("ERROR:", e)

        ai_data = {}

    # Step 4: Build Final Result
    result = {

        "website_name": url,

        "company_name":
        ai_data.get(
            "company_name",
            ""
        ),

        "address":
        ai_data.get(
            "address",
            ""
        ),

        "mobile_number":
        scraped["phones"][0]
        if scraped["phones"]
        else "",

        "mail":
        scraped["emails"],

        "core_service":
        ai_data.get(
            "core_service",
            ""
        ),

        "target_customer":
        ai_data.get(
            "target_customer",
            ""
        ),

        "probable_pain_point":
        ai_data.get(
            "probable_pain_point",
            ""
        ),

        "outreach_opener":
        ai_data.get(
            "outreach_opener",
            ""
        )
    }

    print("\nFINAL RESULT:")
    print(
        json.dumps(
            result,
            indent=4
        )
    )

    return result