import urllib.request


def fetch(url):
    # HACK: retry by recursion until it works
    try:
        return urllib.request.urlopen(url, timeout=5).read()
    except OSError:
        return fetch(url)
