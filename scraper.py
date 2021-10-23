import argparse
from logzero import logger

from reddit_api.comment import CommentSearch
from reddit_api.submission import SubmissionSearch


def main(args):
    logger.info(f"Starting reddit scraper for: {args}")

    submissions = SubmissionSearch(subreddit=args.subreddit).get_submissions

    for submission in submissions:
        if submission.num_comments > 0:
            comment_ids = SubmissionSearch.get_submission_comment_ids(submission_id=submission.id)
            for comment_id in comment_ids:
                comment = CommentSearch.get_comment(comment_id=comment_id)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required subreddit name
    parser.add_argument("subreddit", help="Subreddit name")

    args = parser.parse_args()
    main(args)
