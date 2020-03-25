# -*- coding: utf-8 -*-
import scrapy
from ..items import SaturdayclubglobaltrustItem
from datetime import datetime


class MembersSpider(scrapy.Spider):
    name = "Members"
    allowed_domains = ["http://scgt.org.in"]
    start_urls = [
        'http://scgt.org.in/chapters.aspx'
    ]

    def parse(self, response):
        item = SaturdayclubglobaltrustItem()
        sections = response.xpath('//section[@id="chapter"]')

        for sec in sections:
            item['City'] = sec.xpath('.//h3/text()').extract_first(default='')
            if item['City'] == '':
                item['City'] = sec.xpath('.//h3/strong/text()').extract_first(default='')
            members = sec.xpath('.//article')
            for mem in members:
                item['Name'] = mem.xpath('.//p/strong/text()').extract_first(default='')
                item['Mobile_No'] = ''
                try:
                    item['Mobile_No'] = ';'.join(mem.xpath('.//p/text()').extract()).split('Mobile :')[1].split('Email')[0].strip()
                except:
                    item['Mobile_No'] = ';'.join(mem.xpath('.//p/text()').extract()).split('Phone ')[1].split('Email')[0].strip()
                item['Email_Address'] = ';'.join(mem.xpath('.//p/a/text()').extract()).strip()

                item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')
                item['platform'] = 'http://scgt.org.in/chapters.aspx'

                yield item
