# Start a debug session in this file to debug the spider.
import os
from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'niche',
            '--loglevel',
            'DEBUG',
            '--logfile',
            'log.log',
        ]
    )
except SystemExit:
    pass
