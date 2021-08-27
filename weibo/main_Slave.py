# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

spider_name = 'search'
cmd_string = 'scrapy crawl {spider_name}'.format(spider_name=spider_name)
execute(cmd_string.split())

