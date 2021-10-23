from logzero import logger
from typing import NamedTuple

from reddit_api.reddit_api_client import Client


class Submission(NamedTuple):
    title: str
    selftext: str
    id: str
    upvote_ratio: float
    num_comments: int
    link_flair_text: str
    score: int
    created_utc: int
    author: str
    author_fullname: str
    retrieved_on: int


class SubmissionSearch:
    def __init__(self, subreddit: str, num_of_days: int = 1):
        self.search_parameters = {
            "sort": "desc",
            "subreddit": subreddit,
            "after": num_of_days,
            "fields": ["title", "selftext", "id", "upvote_ratio", "num_comments", "link_flair_text", "score",
                       "created_utc", "author", "author_fullname", "retrieved_on"],
        }

    @property
    def get_submissions(self) -> list[Submission]:
        client = Client(search_parameters=self.search_parameters, url_suffix="reddit/search/submission")
        # Fetching API search results
        try:
            response_json = client.search()
        except Exception as e:
            logger.info(f"Unable to get submissions from reddit API: {e}")
            return []

        # Parsing search results
        if "data" not in response_json:
            logger.info(f"Unable to to parse reddit API response: 'data' field is missing")
            return []

        search_results: list[Submission] = []
        logger.info(f"Parsing received submissions")
        for submission in response_json["data"]:
            try:
                search_results.append(
                    Submission(
                        title=submission["title"],
                        selftext=submission["selftext"],
                        id=submission["id"],
                        upvote_ratio=float(submission["upvote_ratio"]),
                        num_comments=int(submission["num_comments"]),
                        link_flair_text=submission["link_flair_text"],
                        score=int(submission["score"]),
                        created_utc=int(submission["created_utc"]),
                        author=submission["author"],
                        author_fullname=submission["author_fullname"],
                        retrieved_on=int(submission["retrieved_on"]),
                    )
                )
            except ValueError:
                logger.info(f"Unable to to parse reddit API response for submission: {submission}")
                logger.info(f"Continue with other submissions parsing")

        return search_results

    @staticmethod
    def get_submission_comment_ids(submission_id: str) -> list[str]:
        client = Client(search_parameters={}, url_suffix=f"reddit/submission/comment_ids/{submission_id}")

        # Fetching API search results
        try:
            response_json = client.search()
        except Exception as e:
            logger.info(f"Unable to get submission ids from reddit API: {e}")
            return []

        # Parsing search results
        if "data" not in response_json:
            logger.info(f"Unable to to parse reddit API response: 'data' field is missing")
            return []

        return response_json["data"]
