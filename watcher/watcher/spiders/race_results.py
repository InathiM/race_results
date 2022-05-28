import scrapy

class ResultsSpider(scrapy.Spider):
    name = 'results'
    start_urls =[
        'https://www.formula1.com/en/results.html'
    ]


    def parse(self, response):
        title = response.css('title').extract_first()
        table_header = response.css('div.resultsarchive-wrapper').css('.resultsarchive-table tr th::text').extract()
        race_results = response.css('div.resultsarchive-wrapper').css('.resultsarchive-table tr td::text').extract()
        
        
        yield  {
            'titletext':title,
            'tableheader':table_header,
            'results': race_results
        }

