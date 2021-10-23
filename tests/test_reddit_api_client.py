from reddit_api import reddit_api_client as reddit_client
import mock
import pytest


@pytest.fixture
def mock_get_request():
    with mock.patch(
        "reddit_api.reddit_api_client.requests.get",
        autospec=True,
    ) as _mock_requests_get:
        yield _mock_requests_get


def test_search(mock_get_request):
    expected_search_results = {
        "data": [
            {
                "author": "-fckmylife-",
                "author_fullname": "t2_erth9oc6",
                "created_utc": 1634981756,
                "id": "qe1pfe",
                "num_comments": 0,
                "retrieved_on": 1634981767,
                "score": 1,
                "link_flair_text": "Moving to TX",
                "selftext": "I'm a darker skin (medium-brown rather than pale-brown)",
                "upvote_ratio": 2.0,
                "title": "Kind of a loaded question, but how much racism should I realistically expect if I move here?",
            },
        ]
    }

    mock_get_request.return_value.status_code = 200
    mock_get_request.return_value.json.return_value = expected_search_results
    client = reddit_client.Client(search_parameters={}, url_suffix="comment")
    search_results = client.search()
    assert search_results == expected_search_results


def test_search_api_error(mock_get_request):
    expected_search_results = None
    mock_get_request.return_value.status_code = 404
    mock_get_request.return_value.json.return_value = expected_search_results

    client = reddit_client.Client(search_parameters={}, url_suffix="comment")
    with pytest.raises(Exception):
        client.search()
