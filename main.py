from fastapi import FastAPI, Request

import discord
import scraper
from cache import Cache

MAX_EMBEDS = 10

app = FastAPI()


async def scrape_job_posts():
    results = scraper.get_jobs()
    cache = Cache()

    for i in results:
        key = i[0]
        value = i[1]
        items = []

        for index, v in enumerate(value):
            # only accept max of the first 10 job posts
            if index + 1 == MAX_EMBEDS:
                break

            # skip already posted / send to webhook
            if cache.exists(v["uid"]):
                continue

            items.append(v)

            # add item to cache
            cache.put(v["uid"])

        discord.post_to_channel(key["query"], key["location"], items)


@app.post("/__space/v0/actions")
async def sched_actions(request: Request):
    data = await request.json()
    event = data["event"]
    if event["id"] == "scrape":
        await scrape_job_posts()
