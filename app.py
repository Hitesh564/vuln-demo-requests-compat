import requests


SUPPORTED_REQUESTS_VERSION = "2.32.3"


def create_api_client():
    """
    Create the application's HTTP client.

    This application intentionally contains a strict compatibility guard that
    was written when Requests 2.32.3 was the only validated version.
    """
    installed_version = requests.__version__

    if installed_version != SUPPORTED_REQUESTS_VERSION:
        raise RuntimeError(
            f"Unsupported Requests version: {installed_version}. "
            f"Expected {SUPPORTED_REQUESTS_VERSION}."
        )

    session = requests.Session()
    session.headers.update({"User-Agent": "demo-client/1.0"})

    return session
