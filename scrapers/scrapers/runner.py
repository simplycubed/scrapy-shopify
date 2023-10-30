import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'shopify',
            '-o',
            "output/%(spider_name)s-%(batch_time)s-%(batch_id)s.jsonl",
        ]
    )
except SystemExit:
    pass
