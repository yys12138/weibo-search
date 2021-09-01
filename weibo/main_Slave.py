# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import  threading
spider_name = 'search'
#cmd_string = 'scrapy crawl {spider_name}'.format(spider_name=spider_name)i=1
job_id=1


#cmd_string = 'scrapy crawl {spider_name} -s JOBDIR=crawls/{spider_name}-{job_id}'.format(spider_name=spider_name, job_id=job_id)
cmd_string = 'scrapy crawl {spider_name} '.format(spider_name=spider_name, job_id=job_id)

execute(cmd_string.split())



