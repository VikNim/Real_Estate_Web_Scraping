# -*- coding: utf-8 -*-
import scrapy
from selenium.webdriver import Chrome
import logging
from datetime import datetime
from selenium.webdriver.remote.remote_connection import LOGGER
import time
from ..items import ProrealtorsItem


class ProspiderSpider(scrapy.Spider):
    name = "ProSpider"
    allowed_domains = ["http://prorealtors.in/Home/CSAssistList"]
    start_urls = [
        'http://prorealtors.in/Home/CSAssistList',
    ]

    def parse(self, response):
        LOGGER.setLevel(logging.WARNING)
        item = ProrealtorsItem()

        try:
            for i in range(580, 10000):
                driver = Chrome()
                try:
                    driver.get('http://prorealtors.in/Home/Login')
                    time.sleep(2)

                    mail_input = driver.find_element_by_id('txtUserName')
                    mail_input.send_keys('shmalik@black-and-white.in')

                    password_input = driver.find_element_by_id('txtPassword')
                    password_input.send_keys('prorealtor')

                    login_submit = driver.find_element_by_id('btnSubmit')
                    login_submit.click()
                    time.sleep(2)
                except Exception as e:
                    print(e)
                    quit(1)

                try:
                    print('Current No:', i)
                    driver.get('http://prorealtors.in/')
                    time.sleep(2)

                    ca_assist = driver.find_element_by_xpath('//section[@id="main"]/section[1]/section/div/div/ul/li[3]/a')
                    ca_assist.click()
                    time.sleep(2)

                    ca_input = driver.find_element_by_id('txtBuildNameC')
                    ca_input.send_keys(str(i))
                    time.sleep(2)

                    find_ca_assist = driver.find_element_by_xpath('//div[@id="tab3"]/form/div[@class="inner"]/a/button')
                    find_ca_assist.click()
                    time.sleep(2)

                    # print('Windows Handles as of Now : ', driver.window_handles)

                    table_rows = driver.find_elements_by_xpath('/html/body/section[3]/div/div/table/tbody/tr')

                    for row in table_rows[1:]:
                        try:
                            item['Building_Name'] = row.find_element_by_xpath('./td[2]').text
                            item['CS_Info'] = row.find_element_by_xpath('./td[4]').text
                            item['Location'] = row.find_element_by_xpath('./td[6]').text
                            item['platform'] = 'http://prorealtors.in'
                            item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')
                        except:
                            pass
                        finally:
                            yield item
                except:
                    pass
                driver.quit()

        except Exception as e:
            print(e)
