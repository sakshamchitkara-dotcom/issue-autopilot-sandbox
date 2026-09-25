import time

_CACHE = {}


def get(key):
    # TODO: add TTL eviction, this grows forever
    return _CACHE.get(key)


def clear():
    # TODO: expose cache hit/miss counters
    _CACHE.clear()


def put(key, value):
    # FIXME: not thread safe
    _CACHE[key] = (time.time(), value)
