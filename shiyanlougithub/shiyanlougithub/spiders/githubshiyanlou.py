# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem


class GithubshiyanlouSpider(scrapy.Spider):
    name = "githubshiyanlou"

    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmp.format(i) for i in range(1, 5))


    def parse(self, response):
        for repository in response.css('li.public'):
            item = ShiyanlougithubItem({

            'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
            'update_time': repository.xpath('.//relative-time/@datetime').extract_first()})

            yield item
