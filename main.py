from fastapi import FastAPI, Request

app = FastAPI()


async def scrape_job_posts():
    pass


@app.post("/__space/v0/actions")
async def sched_actions(request: Request):
    data = await request.json()
    event = data["event"]
    if event["id"] == "scrape":
        await scrape_job_posts()
