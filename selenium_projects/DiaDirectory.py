# -*- coding: utf-8 -*-
import scrapy
from ..items import DiasupplyDirectoryItem


class DiadirectorySpider(scrapy.Spider):
    name = "DiaDirectory"
    allowed_domains = [""]
    start_urls = ['file:///C:/Users/Vik/Pictures/Directory _ Diasupply - B.html']

    def parse(self, response):
        records = response.xpaht('//*[@id="accordion"]/div')
        companies = DiasupplyDirectoryItem()
        for data in records:
            i = data.xpath('.//div[contains(@id,"collapse")]')
            companies['company_name'] = data.xpath('.//div[@class="company_name"]/text()').extract_first(default='')
            companies['contact_no'] = i.xpath('./div[@class="panel-body"]/div/div[1]').extract_first(default='')
            companies['contact_person'] = i.xpath('').extract_first(default='')
            companies['website'] = i.xpath('').extract_first(default='')
            companies['office_no'] = i.xpath('').extract_first(default='')
            companies['QBC_no'] = i.xpath('').extract_first(default='')
            companies['email_ids'] = i.xpath('').extract()
