# Coders of Bangalore

A Python project for parsing and analyzing raw Instagram profile data from OpenAI followers.

## Description

This repository converts semi-structured Instagram profile text into structured JSON and answers targeted analytics questions.

It is designed to:

- parse raw profile entries from `finaldata.txt`
- extract metrics such as post count, follower count, following count, profile name, category, and bio
- normalize follower/following values like `K` and `M` into numeric values
- compute analytics such as:
  - user with the most posts
  - user with the most followers
  - user following the most people
  - number of unique profile categories

## Files

- `coders-of-bengalore.ipynb` — Jupyter notebook with parsing logic and analytics
- `finaldata.txt` — raw Instagram profile data source
- `output.json` — parsed dataset export
- `answers.json` — final summary results

## Usage

1. Open `coders-of-bengalore.ipynb`.
2. Run the notebook cells to parse the raw text data.
3. Review `output.json` for structured profile data and `answers.json` for the analytics summary.

## Notes

This repository is useful for anyone working with text parsing, basic social media analytics, or semi-structured scraped data in Python.