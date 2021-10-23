from logzero import logger
from typing import NamedTuple, Optional

from reddit_api.reddit_api_client import Client


class Comment(NamedTuple):
    body: str
    id: str
    score: int
    author: str
    parent_id: str
    created_utc: int


class CommentSearch:
    def __init__(self):
        pass

    @staticmethod
    def get_comment(comment_id: str) -> Optional[Comment]:
        search_parameters = {
            "fields": ["body", "id", "score", "author", "parent_id", "created_utc"],
        }

        client = Client(search_parameters=search_parameters, url_suffix=f"reddit/comment/search?ids={comment_id}")

        # Fetching API search results
        try:
            response_json = client.search()
        except Exception as e:
            logger.info(f"Unable to get comments from reddit API: {e}")
            return None

        # Parsing search results
        if "data" not in response_json:
            logger.info(f"Unable to to parse reddit API response: 'data' field is missing")
            return None

        data = response_json['data']

        if len(data) == 0:
            logger.info(f"Comment {comment_id} not found")
            return None

        if len(data) > 1:
            logger.info(f"API returned more than one result: {data}")
            return None

        data_item = data[0]
        try:
            comment = Comment(
                body=data_item["body"],
                id=data_item["id"],
                score=int(data_item["score"]),
                author=data_item["author"],
                parent_id=data_item["parent_id"],
                created_utc=int(data_item["created_utc"]),
            )
        except ValueError:
            logger.info(f"Unable to to parse reddit API response for comment: {data_item}")
            return None

        return comment
