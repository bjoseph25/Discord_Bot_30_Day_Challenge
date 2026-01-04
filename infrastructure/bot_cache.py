from cachetools import TTLCache

# Cache for repsonse times per command+user+args
response_time_cache = TTLCache(maxsize=100, ttl=60)

# Optional cache for actual command result
data_cache = TTLCache(maxsize=100, ttl=60)