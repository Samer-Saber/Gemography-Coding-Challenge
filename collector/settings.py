# -*- coding: utf-8 -*-

# Scrapy settings for collector project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'collector'

SPIDER_MODULES = ['collector.spiders']
NEWSPIDER_MODULE = 'collector.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'collector (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {'collector.pipelines.MongoDBPipeline': 300 }
MONGODB_DB = "theguardian"
MONGODB_COLLECTION = "news"


