# Scrapy settings for alias_scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'alias_scrape'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['alias_scrape.spiders']
NEWSPIDER_MODULE = 'alias_scrape.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

