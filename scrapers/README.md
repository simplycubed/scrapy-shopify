# Shopify Spider

```bash
# execute runner
python runner.py

# execute scraper
scrapy crawl shopify -o "%(spider_name)s-%(batch_time)s-%(batch_id)s.jsonl"

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
