import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, limit=5, window=10):
        self.limit = limit
        self.window = window
        self.requests = defaultdict(list)

    def check(self, key):
        now = time.time()
        window_start = now - self.window

        self.requests[key] = [
            t for t in self.requests[key] if t > window_start
        ]

        if len(self.requests[key]) >= self.limit:
            return False

        self.requests[key].append(now)
        return True
