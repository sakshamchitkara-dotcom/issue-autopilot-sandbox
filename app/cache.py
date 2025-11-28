import time

_CACHE = {}


def get(key):
    # TODO: add TTL eviction, this grows forever
    return _CACHE.get(key)


def put(key, value):
    # FIXME: not thread safe
    _CACHE[key] = (time.time(), value)
