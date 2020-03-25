# -*- coding: utf-8 -*-
import scrapy
from selenium.webdriver import Chrome
from datetime import datetime
from ..items import HudkuItem
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER


class HudkuspiderSpider(scrapy.Spider):
    name = "HudkuSpider"
    allowed_domains = ["www.hudku.com"]
    start_urls = [
        # 'http://www.hudku.com/search/business-list/Real Estate Agents in Mumbai, Maharashtra, India',
        # 'http://www.hudku.com/search/business-list/Real Estate Developers in Maharashtra, India',
        # 'http://www.hudku.com/search/business-list/Apartments in Mumbai, Maharashtra, India',
        # Jewellers
        'http://www.hudku.com/search/business-list/Jewellery in Mumbai, Maharashtra, India',
        'http://www.hudku.com/search/business-list/Diamonds in Mumbai, Maharashtra, India',
        'http://www.hudku.com/search/business-list/Diamonds Retail in Mumbai, Maharashtra, India',
        'http://www.hudku.com/search/business-list/Imitation Jewellery in Mumbai, Maharashtra, India',
        'http://www.hudku.com/search/business-list/Jewellery Valuers in Mumbai, Maharashtra, India',
        'http://www.hudku.com/search/business-list/Jewellery Showrooms %26 Retail in India',
        'http://www.hudku.com/search/business-list/Diamonds in Mumbai, Maharashtra, India',
        # Government Offices
        'http://www.hudku.com/search/business-list/Government Offices in Mumbai, Maharashtra, India',
        'http://www.hudku.com/search/business-list/Registrar Office in Mumbai, Maharashtra, India',
        # Veterinary Clinics & Hospitals in Mumbai, Maharashtra, India
        'http://www.hudku.com/search/business-list/Veterinary Clinics %26 Hospitals in Mumbai, Maharashtra, India',
        # Pet Relatable
        'http://www.hudku.com/search/business-list/Pets in Mumbai, Maharashtra, India',
    ]

    def parse(self, response):
        LOGGER.setLevel(logging.WARNING)
        driver = Chrome()
        item = HudkuItem()

        driver.get(response.url)

        while True:
            try:
                table_rows = driver.find_elements_by_xpath('//table[@id="idTableListings"]/tbody/tr')
                driver.implicitly_wait(10)
                time.sleep(2)

                for row in table_rows:
                    try:
                        item['platform'] = 'www.hudku.com'
                        item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')

                        item['Name'] = row.find_element_by_xpath('.//td/div/div[1]/span[2]').text
                        item['Address'] = row.find_element_by_xpath('.//td/div/div[1]/p[1]/span').text
                        item['Website'] = item['Fax_No'] = item['Email_Id'] = item['Contact_No'] = ''
                        try:
                            item['Contact_No'] = row.find_element_by_xpath('.//td/div/div[2]/div[1]/div[@class="phone"]/span').text
                        except:
                            pass

                        try:
                            item['Email_Id'] = row.find_element_by_xpath('.//td/div/div[2]/div[1]/div[@class="mail_info"]/span').text
                        except:
                            pass

                        try:
                            item['Fax_No'] = row.find_element_by_xpath('.//td/div/div[2]/div[1]/div[@class="fax_info"]/span').text
                        except:
                            pass

                        try:
                            item['Website'] = row.find_element_by_xpath('.//td/div/div[2]/div[1]/div[@class="web_info"]/span').text
                        except:
                            pass
                    except:
                        pass
                    finally:
                        yield item

                more_records = driver.find_element_by_xpath('//*[@id="idPaginationList"]/*//button[@class="next"]')
                more_records.click()
                driver.implicitly_wait(10)
                time.sleep(2)
            except:
                break
        time.sleep(2)
        driver.quit()
