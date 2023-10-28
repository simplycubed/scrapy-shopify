# Shopify Spider

- This project uses a single Scrapy project containing all available Spiders and Scrapers.

## Bright Data - Web Scraping Proxy

- [Bright Data](https://brightdata.com/) - web scraping platform where the website crawlers and website scrapers will execute.

## Tech Stack

- Web Spiders and Scrapers are written in Python using [Scrapy](https://scrapy.org/)
- [Web Crawling with Python](https://brightdata.com/blog/how-tos/web-crawling-with-python)

## Hosting

- Starting with 1 web scraper now (Shopify) but will have 70+ scrapers (1 per marketplace).
- Web scrapers will run in [Cloud Run Jobs (not services)](https://cloud.google.com/run/docs/create-jobs) and will be deployed with GitHub Actions.
- Web scrapers will need to be able to call out (egress) to scrape data and to store the data Google Storage and Firestore.
- Web scraper will be configured with only 1 max instance per marketplace.

## Storage

- Web scrapped data is stored in Google Cloud Storage as JSON line files (.jsonl).
- Cloud Functions are triggered by new files in Google Cloud Storage and will process the data and store it in Firestore and BigQuery.

## Architecture

![Architecture](./assets/architecture.png)
