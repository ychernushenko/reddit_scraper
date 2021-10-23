from reddit_api import comment
import mock
import pytest


@pytest.fixture
def mock_search():
    with mock.patch(
        "reddit_api.reddit_api_client.Client.search",
        autospec=True,
    ) as _mock_search:
        yield _mock_search


def test_get_comment(mock_search):
    search_results = {
        "data": [
            {
                "approved_at_utc": None,
                "author": "Skrt__Skrt",
                "author_flair_css_class": None,
                "author_flair_text": None,
                "banned_at_utc": None,
                "body": "CNN just showed video of the police on TV, right ater saying dont share anything on socia",
                "can_mod_post": False,
                "collapsed": False,
                "collapsed_reason": None,
                "created_utc": 1502988145,
                "distinguished": None,
                "edited": False,
                "id": "dlrawgw",
                "is_submitter": False,
                "link_id": "t3_6uanuh",
                "parent_id": "t3_6uanuh",
                "retrieved_on": 1502988146,
                "score": 1,
                "stickied": False,
                "subreddit": "worldnews",
                "subreddit_id": "t5_2qh13"
            },
        ]
    }

    expected_comment = comment.Comment(
        body="CNN just showed video of the police on TV, right ater saying dont share anything on socia",
        id="dlrawgw",
        score=1,
        author="Skrt__Skrt",
        parent_id="t3_6uanuh",
        created_utc=1502988145,
    )

    mock_search.return_value = search_results
    search_result = comment.CommentSearch.get_comment("dlrawgw")
    assert search_result == expected_comment


def test_get_comment_api_response_missing_data(mock_search):
    mock_search.return_value = {}
    search_result = comment.CommentSearch.get_comment("dlrawgw")
    assert search_result is None


def test_get_comment_api_response_empty_data(mock_search):
    mock_search.return_value = {
        "data": []
    }
    search_result = comment.CommentSearch.get_comment("dlrawgw")
    assert search_result is None


def test_get_comment_api_response_several_entries_in_data(mock_search):
    mock_search.return_value = {
        "data": [
            {
                "approved_at_utc": None,
                "author": "Skrt__Skrt",
                "author_flair_css_class": None,
                "author_flair_text": None,
                "banned_at_utc": None,
                "body": "CNN just showed video of the police on TV, right ater saying dont share anything on socia",
                "can_mod_post": False,
                "collapsed": False,
                "collapsed_reason": None,
                "created_utc": 1502988145,
                "distinguished": None,
                "edited": False,
                "id": "dlrawgw",
                "is_submitter": False,
                "link_id": "t3_6uanuh",
                "parent_id": "t3_6uanuh",
                "retrieved_on": 1502988146,
                "score": 1,
                "stickied": False,
                "subreddit": "worldnews",
                "subreddit_id": "t5_2qh13"
            },
            {
                "approved_at_utc": None,
                "author": "Skrt__Skrt",
                "author_flair_css_class": None,
                "author_flair_text": None,
                "banned_at_utc": None,
                "body": "CNN just showed video of the police on TV, right ater saying dont share anything on socia",
                "can_mod_post": False,
                "collapsed": False,
                "collapsed_reason": None,
                "created_utc": 1502988145,
                "distinguished": None,
                "edited": False,
                "id": "dlrawgw",
                "is_submitter": False,
                "link_id": "t3_6uanuh",
                "parent_id": "t3_6uanuh",
                "retrieved_on": 1502988146,
                "score": 1,
                "stickied": False,
                "subreddit": "worldnews",
                "subreddit_id": "t5_2qh13"
            },
        ]
    }
    search_result = comment.CommentSearch.get_comment("dlrawgw")
    assert search_result is None


def test_get_comment_api_response_wrong_data_type(mock_search):
    mock_search.return_value = {
        "data": [
            {
                "approved_at_utc": None,
                "author": "Skrt__Skrt",
                "author_flair_css_class": None,
                "author_flair_text": None,
                "banned_at_utc": None,
                "body": "CNN just showed video of the police on TV, right ater saying dont share anything on socia",
                "can_mod_post": False,
                "collapsed": False,
                "collapsed_reason": None,
                "created_utc": "wrong_type",
                "distinguished": None,
                "edited": False,
                "id": "dlrawgw",
                "is_submitter": False,
                "link_id": "t3_6uanuh",
                "parent_id": "t3_6uanuh",
                "retrieved_on": 1502988146,
                "score": 1,
                "stickied": False,
                "subreddit": "worldnews",
                "subreddit_id": "t5_2qh13"
            },
        ]
    }

    search_result = comment.CommentSearch.get_comment("dlrawgw")
    assert search_result is None


def test_get_submissions_api_exception(mock_search):
    mock_search.side_effect = Exception()
    search_result = comment.CommentSearch.get_comment("dlrawgw")
    assert search_result is None
