# -*- coding: utf-8 -*-
import scrapy
from ..items import SaturdayclubglobaltrustItem
from datetime import datetime


class BoardmembersSpider(scrapy.Spider):
    name = "BoardMembers"
    allowed_domains = ["scgt.org.in"]
    start_urls = [
        'http://scgt.org.in/organization.aspx',
    ]

    def parse(self, response):
        item = SaturdayclubglobaltrustItem()
        sections = response.xpath('//section[@id="chapter"]/article')

        for mem in sections:
            item['City'] = 'Mumbai'
            item['Name'] = mem.xpath('.//p/strong/text()').extract_first(default='')
            item['Mobile_No'] = ''
            try:
                item['Mobile_No'] = ';'.join(mem.xpath('.//p/text()').extract()).split('Mobile :')[1].split('Email')[0].strip()
            except:
                item['Mobile_No'] = ';'.join(mem.xpath('.//p/text()').extract()).split('Phone ')[1].split('Email')[
                    0].strip()
            item['Email_Address'] = ';'.join(mem.xpath('.//p/a/text()').extract()).strip()

            item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')
            item['platform'] = 'http://scgt.org.in/organization.aspx'

            yield item