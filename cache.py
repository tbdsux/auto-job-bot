from datetime import datetime
from typing import TypedDict

from deta import Deta


class CacheJob(TypedDict):
    key: str  # job uid
    date_added: str


class Cache:
    def __init__(self) -> None:
        self.deta = Deta()
        self.base = self.deta.Base("cache_jobs")

    def put(self, uid: str):
        item_cache: CacheJob = {"key": uid, "date_added": datetime.now().isoformat()}
        self.base.put(item_cache)

    def exists(self, uid: str):
        item = self.base.get(uid)
        if item is None:
            return False

        return True
