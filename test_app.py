from app import create_api_client


def test_create_api_client():
    client = create_api_client()

    assert client is not None
    assert client.headers["User-Agent"] == "demo-client/1.0"
