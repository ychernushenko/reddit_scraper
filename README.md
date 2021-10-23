# Reddit Scraper

This project allows scraping Reddit submissions and comments from https://api.pushshift.io/ endpoint to save them
locally in AVRO format.

## Requirements

- tested for python 3.9.7

### Setup

`pip install virtualenv`  
`virtualenv venv`  
`source ./venv/bin/activate`    
`pip install -r requirements.txt`

## Run

`python ./scraper.py subreddit='tidal'`

### Maintain daily

Setup for cron to run daily

## Architecture

### Diagram

### Project structure

### Limitations and trade-offs

- For simplicity of implementation for every comment there is a separate request, this could be optimized, using search
  api with several ids
-

### Data quality

- Field 'author_fullname' is missing in API return values

### Testing approach

### Logs

Logs are written in standard output

### Error handling

- No verification on duplicates
- Data types are verified, non-matching are skipped
- Entries with missing fields are skipped
- Entries with missing fields are skipped
- Too big text replies are not verified
- Pagination is not handled
- Situation when submission has a lot of comments (thousands) was not tested

## Running all tests

`pytest`
