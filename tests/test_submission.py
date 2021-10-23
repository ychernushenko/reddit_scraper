from reddit_api import submission
import mock
import pytest


@pytest.fixture
def mock_search():
    with mock.patch(
        "reddit_api.reddit_api_client.Client.search",
        autospec=True,
    ) as _mock_search:
        yield _mock_search


def test_get_submissions(mock_search):
    search_results = {
        "data": [
            {
                "author": "-fckmylife-",
                "author_fullname": "t2_erth9oc6",
                "created_utc": 1634981756,
                "id": "qe1pfe",
                "num_comments": 0,
                "link_flair_text": "Moving to TX",
                "retrieved_on": 1634981767,
                "score": 1,
                "selftext": "I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
                "upvote_ratio": 2.0,
                "title": "Kind of a loaded question, but how much racism should I realistically expect if I move here?",
            },
            {
                "all_awardings": [],
                "allow_live_comments": False,
                "author": "-fckmylife-",
                "author_flair_css_class": None,
                "author_flair_richtext": [],
                "author_flair_text": None,
                "author_flair_type": "text",
                "author_fullname": "t2_erth9oc6",
                "author_is_blocked": False,
                "author_patreon_flair": False,
                "author_premium": False,
                "awarders": [],
                "can_mod_post": False,
                "contest_mode": False,
                "created_utc": 1634981756,
                "domain": "self.texas",
                "full_link": "https://www.reddit.com/r/texas/comments/qe1pfr/kind_of_a_loaded_question_but_how_much_racism/",
                "gildings": {},
                "id": "qe1pfr",
                "is_created_from_ads_ui": False,
                "is_crosspostable": True,
                "is_meta": False,
                "is_original_content": False,
                "is_reddit_media_domain": False,
                "is_robot_indexable": True,
                "is_self": True,
                "is_video": False,
                "link_flair_background_color": "#373c3f",
                "link_flair_richtext": [
                    {
                        "e": "text",
                        "t": "Moving to TX"
                    }
                ],
                "link_flair_template_id": "ed4c92b8-bd04-11e9-94d1-0ec3436af2c8",
                "link_flair_text": "Moving to TX",
                "link_flair_text_color": "light",
                "link_flair_type": "richtext",
                "locked": False,
                "media_only": False,
                "no_follow": True,
                "num_comments": 0,
                "num_crossposts": 0,
                "over_18": False,
                "parent_whitelist_status": "all_ads",
                "permalink": "/r/texas/comments/qe1pfr/kind_of_a_loaded_question_but_how_much_racism/",
                "pinned": False,
                "post_hint": "self",
                "preview": {
                    "enabled": False,
                    "images": [
                        {
                            "id": "Qi2Mr9schC2c2t0iLG2qJJgLaIA7-A5w_0gSUZ0nLcQ",
                            "resolutions": [
                                {
                                    "height": 81,
                                    "url": "https://external-preview.redd.it/boK21ORryvmsuZjGBM-R3WwZiQEf3hJMjoPk5DyTPZw.jpg?width=108&amp;crop=smart&amp;auto=webp&amp;s=691a885598bcda8ca4b5814d087326d1781459bc",
                                    "width": 108
                                },
                                {
                                    "height": 162,
                                    "url": "https://external-preview.redd.it/boK21ORryvmsuZjGBM-R3WwZiQEf3hJMjoPk5DyTPZw.jpg?width=216&amp;crop=smart&amp;auto=webp&amp;s=4a19eb41812a29b4fed3f4e6cd54f03c919a8c77",
                                    "width": 216
                                },
                                {
                                    "height": 240,
                                    "url": "https://external-preview.redd.it/boK21ORryvmsuZjGBM-R3WwZiQEf3hJMjoPk5DyTPZw.jpg?width=320&amp;crop=smart&amp;auto=webp&amp;s=d2b023145f4c2484224506b1924b7e37876a0a4d",
                                    "width": 320
                                }
                            ],
                            "source": {
                                "height": 360,
                                "url": "https://external-preview.redd.it/boK21ORryvmsuZjGBM-R3WwZiQEf3hJMjoPk5DyTPZw.jpg?auto=webp&amp;s=01640e0af66247514955887d2df817c71b05a9ff",
                                "width": 480
                            },
                            "variants": {}
                        }
                    ]
                },
                "pwls": 6,
                "retrieved_on": 1634981767,
                "score": 1,
                "selftext": "I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
                "send_replies": True,
                "spoiler": False,
                "stickied": False,
                "subreddit": "texas",
                "subreddit_id": "t5_2qho4",
                "subreddit_subscribers": 363325,
                "subreddit_type": "public",
                "suggested_sort": "confidence",
                "thumbnail": "self",
                "title": "Kind of a loaded question, but how much racism should I realistically expect if I move here?",
                "total_awards_received": 0,
                "treatment_tags": [],
                "upvote_ratio": 1.0,
                "url": "https://www.reddit.com/r/texas/comments/qe1pfr/kind_of_a_loaded_question_but_how_much_racism/",
                "whitelist_status": "all_ads",
                "wls": 6
            },
        ]
    }

    expected_submissions = [
        submission.Submission(
            title="Kind of a loaded question, but how much racism should I realistically expect if I move here?",
            selftext="I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
            id="qe1pfe",
            upvote_ratio=2.0,
            num_comments=0,
            link_flair_text="Moving to TX",
            score=1,
            created_utc=1634981756,
            author="-fckmylife-",
            author_fullname="t2_erth9oc6",
            retrieved_on=1634981767,
        ),
        submission.Submission(
            title="Kind of a loaded question, but how much racism should I realistically expect if I move here?",
            selftext="I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
            id="qe1pfr",
            upvote_ratio=1.0,
            num_comments=0,
            link_flair_text="Moving to TX",
            score=1,
            created_utc=1634981756,
            author="-fckmylife-",
            author_fullname="t2_erth9oc6",
            retrieved_on=1634981767,
        )
    ]

    mock_search.return_value = search_results
    submission_search = submission.SubmissionSearch(subreddit='test_subreddit')
    submissions = submission_search.get_submissions
    assert submissions == expected_submissions


def test_get_submissions_api_response_missing_data(mock_search):
    mock_search.return_value = {}
    submission_search = submission.SubmissionSearch(subreddit='test_subreddit')
    submissions = submission_search.get_submissions
    assert submissions == []


def test_get_submissions_api_response_wrong_data_type(mock_search):
    mock_search.return_value = {
        "data": [
            {
                "title": "Kind of a loaded question, but how much racism should I realistically expect if I move here?",
                "selftext": "I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
                "id": "qe1pfr",
                "upvote_ratio": "qwe",
                "num_comments": 0,
                "link_flair_text": "Moving to TX",
                "score": 1,
                "created_utc": 1634981756,
                "author": "-fckmylife-",
                "author_fullname": "t2_erth9oc6",
                "retrieved_on": 1634981767,
            },
            {
                "title": "Kind of a loaded question, but how much racism should I realistically expect if I move here?",
                "selftext": "I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
                "id": "qe1pfr",
                "upvote_ratio": 2.0,
                "num_comments": 0,
                "link_flair_text": "Moving to TX",
                "score": 1,
                "created_utc": 1634981756,
                "author": "-fckmylife-",
                "author_fullname": "t2_erth9oc6",
                "retrieved_on": 1634981767,
            },
        ]
    }

    expected_submissions = [
        submission.Submission(
            title="Kind of a loaded question, but how much racism should I realistically expect if I move here?",
            selftext="I'm a darker skin (medium-brown rather than pale-brown) Arab Muslim. I grew up in Canada and am currently getting a degree in Computer Science. I wanna move to America once I graduate, and ideally I'd move to Texas rather than California or New York because of stuff like the lower real estate prices and the right to conceal-carry for self-defense. I think if Republicans/right-wingers got to know me they'd find we have a lot in common (I'm centrist/center-left), the only possible issues I can think of are that I smoke weed all the time. I really believe in the American Dream and the idea resonates with me, but sometimes I get uncomfortable around what a consider blind patriots/ultra-nationalists and I feel like because of my ethno-religious background I might get accused of being unamerican or a potential traitor if I critique US government policies. \n\nI also want my future kids to not lose their cultural roots while integrating, and to not feel ashamed of their background. And I wanna make sure that if they get in a fight in high school or a bar fight or something, that they're not discriminated against by the school administration or the police. I'm concerned about LA/NYC's school curriculum and how they advocate for stuff like [encouraging transgender kids to start going on hormones and doing the transition at extremely young ages](https://www.youtube.com/watch?v=Dc5G0v02OMw), but at the same time it's almost guaranteed we won't face significant racism there whereas Texas has a bit of a reputation for it.",
            id="qe1pfr",
            upvote_ratio=2.0,
            num_comments=0,
            link_flair_text="Moving to TX",
            score=1,
            created_utc=1634981756,
            author="-fckmylife-",
            author_fullname="t2_erth9oc6",
            retrieved_on=1634981767,
        )
    ]

    submission_search = submission.SubmissionSearch(subreddit='test_subreddit')
    submissions = submission_search.get_submissions
    assert submissions == expected_submissions


def test_get_submissions_api_exception(mock_search):
    mock_search.side_effect = Exception()

    submission_search = submission.SubmissionSearch(subreddit='test_subreddit')
    submissions = submission_search.get_submissions
    assert submissions == []


def test_get_submission_comment_ids(mock_search):
    search_results = {
        "data": [
            "dls663o",
            "dls67q6",
            "dls6fgv",
            "dls6fqj",
            "dls6kii",
            "dls6kkm",
        ]
    }

    mock_search.return_value = search_results
    comment_ids = submission.SubmissionSearch.get_submission_comment_ids(submission_id="test_id")
    assert comment_ids == search_results["data"]


def test_get_submission_comment_ids_api_response_missing_data(mock_search):
    mock_search.return_value = {}
    comment_ids = submission.SubmissionSearch.get_submission_comment_ids(submission_id="test_id")
    assert comment_ids == []


def test_get_comments_ids_api_exception(mock_search):
    mock_search.side_effect = Exception()
    comment_ids = submission.SubmissionSearch.get_submission_comment_ids(submission_id="test_id")
    assert comment_ids == []
