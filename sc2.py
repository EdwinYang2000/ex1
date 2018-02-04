#!/usr/local/anaconda3/bin/python3

import scrapy

class ShiyanlouGithubSpier(scrapy.Spider):
    name = 'shiyanlougithub'

    @property
    def start_urls(self):
        url_tmp ='https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmp.format(i) for i in range(1,4))

    def parse(self,response):
        for project in response.css('div.position-relative'):
            yield{
                'name': response.css('div.mb-1 h3 a::text').extract(),
                'update_time': response.css('div.mt-2 relative-time::attr(datetime)').extract()
            }