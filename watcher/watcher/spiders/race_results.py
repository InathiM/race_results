from tracemalloc import start
from turtle import title
import scrapy

class ResultsSpider(scrapy.Spider):
    name = 'results'
    start_urls =[
        'https://www.formula1.com/en/results.html'
    ]


    def parse(self, response):
        title = response.css('title::text').extract()
        yield  {
            'titletext':title
        }

