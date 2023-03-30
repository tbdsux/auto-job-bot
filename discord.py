import os
from datetime import datetime
from typing import List

import requests
from job_scraper.types import SearchResult


def create_job_posts(query: str, location: str, items: List[SearchResult]):
    now = datetime.now()

    content = f"""
Query: {query}
Location: {location}
Date: {now.strftime("%B %d, %Y | %I:%M %p")}
    """

    embeds = []
    for i in items:
        em = {
            "title": i["title"],
            "description": i["description"],
            "url": i["link"],
            "author": {"name": f"{i['company']} - {i['location']}"},
            "timestamp": now.isoformat(),
        }

        if i["listed_date"] != "":
            em["footer"] = {"text": i["listed_date"]}

        embeds.append(em)

    if len(embeds) == 0:
        content += """

No new jobs
        """

    return {"content": content, "embeds": embeds, "attachments": []}


def post_to_channel(query: str, location: str, items: List[SearchResult]):
    webhook = os.getenv("WEBHOOK")
    if webhook is None:
        raise Exception("WEBHOOK env not defined.")

    jsonData = create_job_posts(query, location, items)

    r = requests.post(webhook, json=jsonData)
    if not r.ok:
        print(r.json())
        return False

    return True
