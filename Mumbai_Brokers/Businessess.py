# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from ..items import SaturdayclubglobaltrustItem


class BusinessessSpider(scrapy.Spider):
    name = "Businessess"
    allowed_domains = ["http://scgt.org.in"]
    start_urls = [
        'http://members.scgt.org.in/?page_id=6&category=thane',
        'http://members.scgt.org.in/?page_id=6&category=bhandup',
        'http://members.scgt.org.in/?page_id=6&category=dadar',
        'http://members.scgt.org.in/?page_id=6&category=dombivali',
        'http://members.scgt.org.in/?page_id=6&category=kalyan-3',
        'http://members.scgt.org.in/?page_id=6&category=kurla',
        'http://members.scgt.org.in/?page_id=6&category=mulund-west',
        'http://members.scgt.org.in/?page_id=6&category=vashi',
        'http://members.scgt.org.in/?page_id=6&category=borivali',
        'http://members.scgt.org.in/?page_id=6&category=mulund-east',
    ]
    custom_settings = {
        'DOWNLOAD_DELAY': 3.0
    }

    def parse(self, response):
        item = SaturdayclubglobaltrustItem()

        item['Locality'] = response.xpath('//*[@id="wpbdp-category-page"]/h2/text()').extract_first(default='Mumbai').strip()
        data = response.xpath('//div[contains(@id,"wpbdp-listing-")]')

        for div in data:
            item['Business_Name'] = div.xpath('.//div[2]/div[1]/span/a/text()').extract_first(default='')

            item['Business_Category'] = div.xpath('.//div[2]/div[2]/span/a/text()').extract_first(default='')

            item['Address'] = div.xpath('.//div[2]/div[3]/span/text()').extract_first(default='')

            item['Contact_Person'] = div.xpath('.//div[2]/div[4]/span/text()').extract_first(default='')

            item['Business_Contact'] = div.xpath('.//div[2]/div[5]/span/text()').extract_first(default='')

            item['Mobile_No'] = div.xpath('.//div[2]/div[6]/span/text()').extract_first(default='')

            item['Website'] = div.xpath('.//div[2]/div[7]/span/a/text()').extract_first(default='')

            item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')
            item['platform'] = 'http://members.scgt.org.in'

            yield item
