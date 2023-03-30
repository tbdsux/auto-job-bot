import json
from typing import List, TypedDict

from job_scraper import Jora
from job_scraper.types import SearchResult

jora = Jora()


class ItemQuery(TypedDict):
    query: str
    location: str


def get_queries():
    with open("./queries.json", "r") as f:
        d: List[ItemQuery] = json.loads(f.read())

    return d


def get_jobs():
    queries = get_queries()

    results: List[List[ItemQuery, List[SearchResult]]] = []
    for i in queries:
        r = jora.search(i["query"], i["location"])
        results.append([i, r])

    return results
