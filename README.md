# Reddit Scraper

This project allows scraping Reddit submissions and comments from https://api.pushshift.io/ endpoint to save them
locally in Parquet format.

## Requirements

- tested for python 3.9.7

### Setup

`pip install virtualenv`  
`virtualenv venv`  
`source ./venv/bin/activate`    
`pip install -r requirements.txt`

## Run

`python ./scraper.py --subreddit='tidal' --days=7`

## Data interpretation

Data is saved into data folder and partitioned by date (field `created_date` is added to both datasets). Script is
loading all `submissions` for the defined period (one day by default) and all `comments` for these submissions only (
defined period is not used for these load). When script is run twice within a short period of time, data would be
duplicated, because it is saved in the `append` mode.

## Sample output

Check `data` folder

### Limitations and trade-offs

- For simplicity of implementation for every comment there is a separate request, this could be optimized, using search
  api with several ids
- Code was not tested on spark cluster

### Testing approach

Unit tests are written and could be run by `pytest`. Integration test was done manually.

### Logs

Logs are written in standard output

### Error handling and Data quality

- Field `author_fullname` is missing in API return values for `comments`
- No verification on duplicates
- Data types are verified, non-matching entries from API are ignored
- Entries from API with missing fields are ignored
- Too big text replies are not verified
- Pagination is not handled
- Situation when submission has a lot of comments (thousands) was not tested
