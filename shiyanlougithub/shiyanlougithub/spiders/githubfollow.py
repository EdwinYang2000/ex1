# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import MulitpageGithubItem


class GithubfollowSpider(scrapy.Spider):
    name = 'githubfollow'

    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?tab=repositories&page={}'
        return (url_tmp.format(i) for i in range(1, 5))

    def parse(self, response):
        for repository in response.css('li.public'):
            item = MulitpageGithubItem()
            item['name'] = repository.css('div.mb-1 a::text').re_first('\n\s*(.*)')
            item['update_time'] = repository.css('relative-time::attr(datetime)').extract_first()

            repository_url = response.urljoin(repository.xpath('.//a/@href').extract_first())
            print (repository_url)
            request = scrapy.Request(repository_url, callback=self.parse_author)
            request.meta['item'] = item
            yield request

    def parse_author(self,response):

            item = response.meta['item']
            item['commits'] = response.css('li a span.text-emphasized::text').re('\n\s*(.*)')[0]
            item['branches'] = response.css('li a span.text-emphasized::text').re('\n\s*(.*)')[2]
            item['releases'] = response.css('li span.text-emphasized::text').re('\n\s*(.*)')[4]
            yield item