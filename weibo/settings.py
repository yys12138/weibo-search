# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
#LOG_LEVEL = 'CRITICAL'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
#DOWNLOAD_DELAY = 10

ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.Data2MongoDBPipeline': 301,
    #'weibo.pipelines.CsvPipeline': 301,
    # 'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['TCL电视']  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 0
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用”全部“
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2021-08-01'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2021-08-24'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
# MYSQL_HOST = 'localhost'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = '123456'
# MYSQL_DATABASE = 'weibo'

## ========== 防封配置 start ==========

# 1、降低请求速率
# 并发数量 默认16
CONCURRENT_REQUESTS = 80

# Twisted IO线程池的最大大小，默认10
REACTOR_THREADPOOL_MAXSIZE = 50

# 下载超时时间
DOWNLOAD_TIMEOUT = 30

# 禁用重试
RETRY_ENABLED = False

# 2、是否遵循robots.txt协议
ROBOTSTXT_OBEY = False

# 3、禁用cookie
COOKIES_ENABLED = False

# 4、模拟浏览器，注意这里没有配置USER_AGENT！！！
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': '_T_WM=82689783695; SCF=AkmB5XwoF6fjk-xMGCAgCDtsG8K4D8OPgKtAkHT_EG5DkCnXGh0ejo4lKFBPFnKsqI6KxFl9T0-z6KqkR73GZw8.; '
              'SUB=_2A25MIPvDDeRhGeNG6lsU-CbMyTmIHXVv6oWLrDV6PUJbktCOLWz6kW1NS2Ius0EhOCnhLkLccWb0r-ztXGz67wSv; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW7PI-x.h46o4xd2mKXRMzd5NHD95Qf1h24SKnRehzfWs4DqcjZIrH0UGULMcyaU7tt; '
              'SSOLoginState=1629784980; MLOGIN=1; M_WEIBOCN_PARAMS=luicode%3D20000174; WEIBOCN_FROM=1110106030',
   'Connection': 'keep-alive'
}
# 5、使用动态USER_AGENT
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# 6、使用西刺免费代理IP：http://www.xici.net.co/
FREE_PROXY_IPS = [
    {'ip_port': '121.40.78.138:3128', 'user_pass': ''},
]

# 7、使用阿布云收费代理IP：https://www.abuyun.com/http-proxy/dyn-manual-python.html
# 阿布云代理服务器地址
ABU_PROXY_SERVER = 'http://http-dyn.abuyun.com:9020'
# 阿布云代理隧道验证信息,注册阿布云购买服务后获取
ABU_PROXY_USER = 'H291E79V06P40Y0D'
ABU_PROXY_PASS = '18EAB3A55A66A339'

# 阿布云动态ip默认是1秒钟请求5次，（可以加钱，购买多次）。所以，当他是默认5次的时候，我需要对爬虫进行限速
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # 初始下载延迟
DOWNLOAD_DELAY = 8  # 延迟下载间隔

WD_RANDOM_DELAY = 10  # 自定义延迟间隔

# 8、 配置 动态USER_AGENT 和 代理IP 生效，0-1000 配置优先级，数字越小优先级越高
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,

    # 禁用框架默认启动的 UserAgentMiddleware
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    # 启用自定义的随机USER_AGENT RandomUserAgentMiddleware
    'weibo.middlewares.RandomUserAgentMiddleware': 1,

    # # 启用异常处理 ProcessAllExceptionMiddleware
    'weibo.middlewares.ProcessAllExceptionMiddleware': 3,
    #
    # # 启用阿布云代理IP ABuProxyMiddleware
    'weibo.middlewares.ABuProxyMiddleware': 2,
    # 启用免费代理IP FreeProxyMiddleware
    # 'doubanVideoSpiderSlave.middlewares.FreeProxyMiddleware': 2,

    # 随机延迟
    "weibo.middlewares.RandomDelayMiddleware": 999
}

## ========== 防封配置 end ==========


# === 本地环境 start ===

# REDIS
REDIS_HOST = "127.0.0.1"
# 端口号，默认是6379
REDIS_PORT = 6379
REDIS_LIST_KEY = 'wd_baidutieba_康佳'

# MONGODB
MONGODB_HOST = '127.0.0.1'
# 端口号，默认是27017
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = 'wd_weibo'
MONGODB_DOCNAME = 'wd_weibo_TCL'
# === 本地环境 end ===
