# Shopify Spider

- Web scrapped data is stored in Google Cloud Platform and Firestore

## Bright Data - Web Scraping Proxy

- [Bright Data](https://brightdata.com/) - web scraping platform where the website crawlers and website scrapers will execute.

## Tech stack

- Web Spiders and Scrapers are written in Python using [Scrapy](https://scrapy.org/)
- [Web Crawling with Python](https://brightdata.com/blog/how-tos/web-crawling-with-python)

## Hosting

- Starting with 1 web scraper now (Shopify) but will have 70+ scrapers (1 per marketplace).
- Web scrapers will run in [Cloud Run Jobs (not services)](https://cloud.google.com/run/docs/create-jobs) and will be deployed with GitHub Actions.
- Web scrapers will need to be able to call out (egress) to scrape data and to store the data Google Storage and Firestore.
- Web scraper will be configured with only 1 max instance per marketplace.

## Architecture

![Architecture](./assets/architecture.png)

## Examples

```bash
# execute scraper
scrapy crawl shopify -o apps.json

# validating selectors
scrapy shell https://apps.shopify.com/inbox
```

```xml

# <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
#   <url>
#     <loc>https://apps.shopify.com/cleverppc</loc>
#     <lastmod>2023-07-13</lastmod>
#     <changefreq>daily</changefreq>
#     <priority>0.8</priority>
#   </url>
...
```