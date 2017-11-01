# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem


class GithubshiyanlouSpider(scrapy.Spider):
    name = "githubshiyanlou"

    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmp.format(i) for i in range(1, 4))

    def parse(self, response):
        for githubshiyanlou in response.css('div.position-relative'):
            item = ShiyanlougithubItem ({
                'name': response.css('div.mb-1 h3 a::text').re_first("\n\s*(.*)"),
                'update_time': response.css('div.mt-2 relative-time::attr(datetime)').extract_first(),
            })

            yield item
