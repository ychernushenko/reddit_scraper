import argparse

from logzero import logger

from reddit_api.comment import CommentSearch, Comment
from reddit_api.submission import SubmissionSearch, Submission
from pyspark.sql import SparkSession


def main(args):
    logger.info(f"Starting reddit scraper for: {args}")

    num_of_days = args.days
    if not num_of_days.isnumeric():
        logger.info(f"Non-numeric value for num_of_days was given: {num_of_days}")
        return

    submissions = SubmissionSearch(subreddit=args.subreddit, num_of_days=int(num_of_days)).get_submissions

    if len(submissions) == 0:
        logger.info(f"No submissions found for the selected time period")
        return

    spark = SparkSession.builder.appName('reddit.scraper.com').getOrCreate()
    submission_columns = list(Submission._fields)
    submissions_df = spark.createDataFrame(data=submissions, schema=submission_columns)
    submissions_df.write.partitionBy("created_at").mode("append").parquet(f"./data/submissions.parquet")

    comments = []
    for submission in submissions:
        if submission.num_comments > 0:
            comment_ids = SubmissionSearch.get_submission_comment_ids(submission_id=submission.id)
            for comment_id in comment_ids:
                comment = CommentSearch.get_comment(comment_id=comment_id)
                comments.append(comment)

    if len(comments) > 0:
        comments_columns = list(Comment._fields)
        comments_df = spark.createDataFrame(data=comments, schema=comments_columns)
        comments_df.write.partitionBy("created_at").mode("append").parquet(f"./data/comments.parquet")
    logger.info(f"Data saved in ./data folder")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required subreddit name
    parser.add_argument("--subreddit", help="Subreddit name", required=True)

    # Optional number of days
    parser.add_argument("--days", help="Number of days", default=1)

    args = parser.parse_args()
    main(args)
