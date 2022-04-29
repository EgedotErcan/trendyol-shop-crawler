import scrapy
from scrapy.crawler import CrawlerProcess
import json


class TrendyolCrawler( scrapy.Spider ):

    name = 'TrendyolCrawler'

    def start_requests(self):
        urls = ['https://www.trendyol.com/sr?mid=319&os=2&pi=' + str(x) for x in range(1,52)]
        for url in urls:
            yield scrapy.Request(url = url , callback = self.parse_item)

    def parse_item(self,response):
        title_ext = response.css('span.prdct-desc-cntnr-name::text').extract()
        price_ext = response.css('div.prc-box-dscntd::text').extract()
        file_path = 'trendyol_datas.csv'
        with open( file_path , 'a',) as file:
            file.writelines( [title+','+price + '\n' for title,price in zip(title_ext,price_ext)] )
        

  

process = CrawlerProcess()
process.crawl(TrendyolCrawler)
process.start()
