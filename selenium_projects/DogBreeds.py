# -*- coding: utf-8 -*-
import scrapy
from ..items import DoglicensesItem
from datetime import datetime


class DogbreedsSpider(scrapy.Spider):
    name = "DogBreeds"
    allowed_domains = ["https://en.wikipedia.org"]
    start_urls = [
        # 'https://en.wikipedia.org/wiki/List_of_dog_breeds',
        'https://en.wikipedia.org/wiki/List_of_cat_breeds',
    ]

    def parse(self, response):
        item = DoglicensesItem()

        # records = response.xpath('//div[@id="mw-content-text"]/table/tr')
        records = response.xpath('//*[@id="mw-content-text"]/table[2]/tr')

        for dog in records:
            item['dog_name'] = dog.xpath('./td[1]/a/text()').extract_first(default='')
            item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')
            item['platform'] = response.url

            yield item
