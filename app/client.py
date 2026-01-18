import urllib.request


def fetch(url, attempts=3):
    for n in range(attempts):
        try:
            return urllib.request.urlopen(url, timeout=5).read()
        except OSError:
            if n == attempts - 1:
                raise
