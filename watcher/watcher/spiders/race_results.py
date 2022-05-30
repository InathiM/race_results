import scrapy
import pandas as pd

class ResultsSpider(scrapy.Spider):
    name = 'results'
    start_urls =[
        'https://www.formula1.com/en/results.html'
    ]


    def parse(self, response):
        #Get page tittle
        title = str((response.xpath('//title/text()').extract_first())).strip('\n')     
        
        #Create DataFrame and give it column names
        table_header = response.css('.resultsarchive-table tr th::text').extract()
        data = pd.DataFrame(columns = table_header)

        #Get Race Results
        race_results = str(response.css('.resultsarchive-table tr td::text').extract())
        # raceresults = pd.DataFrame(race_results)
        raceresults = pd.DataFrame(race_results)

        
# row_format ="{:>15}" * (len(teams_list) + 1)
# print(row_format.format("", *teams_list))
# for team, row in zip(teams_list, data):
#     print(row_format.format(team, *row))        
        
        yield  {
            'titletext':title,
            'tableheader':table_header,
            'results': race_results
        }

