# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time
from ..items import DoglicensesItem
from datetime import datetime
import logging
from selenium.webdriver.remote.remote_connection import LOGGER


class DogownersSpider(scrapy.Spider):
    name = "DogOwners"
    allowed_domains = ["www.mcgm.gov.in"]
    start_urls = [
        'http://www.mcgm.gov.in/irj/portal/anonymous/qldoglican?guest_user=english',
    ]

    def parse(self, response):
        LOGGER.setLevel(logging.WARNING)

        item = DoglicensesItem()
        driver = webdriver.Chrome()

        driver.get('http://www.mcgm.gov.in/irj/portal/anonymous/qldoglican?guest_user=english')
        time.sleep(5)
        driver.implicitly_wait(5)

        try:
            driver.switch_to.frame(driver.find_element_by_id('ivuFrm_page0ivu0'))
            time.sleep(3)
            driver.implicitly_wait(5)

            driver.switch_to.frame(driver.find_element_by_xpath('//frameset[1]/frame[1]'))
            time.sleep(3)
            driver.implicitly_wait(5)

            first_ward_no = driver.find_element_by_id('WD1C')
            first_ward_no.clear()
            first_ward_no.send_keys('50000226')

            second_ward_no = driver.find_element_by_id('WD20')
            second_ward_no.clear()
            second_ward_no.send_keys('50000227')

            search_records = driver.find_element_by_id('WD5B')
            search_records.click()
            time.sleep(5)

            while True:
                try:
                    table_rows = driver.find_elements_by_xpath('//td[@id="WD62-content"]/table/tbody/tr')

                    for rows in table_rows[1:]:
                        try:
                            item['ward'] = rows.find_element_by_xpath('.//td[2]/span').text

                            item['valid_from'] = rows.find_element_by_xpath('.//td[3]').text

                            item['valid_to'] = rows.find_element_by_xpath('.//td[4]').text

                            item['house_no'] = rows.find_element_by_xpath('.//td[5]').text

                            item['house_name'] = rows.find_element_by_xpath('.//td[6]').text

                            item['street_no'] = rows.find_element_by_xpath('.//td[7]').text

                            item['area'] = rows.find_element_by_xpath('.//td[8]').text

                            item['area1'] = rows.find_element_by_xpath('.//td[9]').text

                            item['postal_code'] = rows.find_element_by_xpath('.//td[10]').text

                            item['tele_no'] = rows.find_element_by_xpath('.//td[11]').text

                            item['dog_name'] = rows.find_element_by_xpath('.//td[12]').text

                            item['gender'] = rows.find_element_by_xpath('.//td[13]').text

                            item['breed'] = rows.find_element_by_xpath('.//td[14]').text

                            item['age_year'] = rows.find_element_by_xpath('.//td[15]').text

                            item['age_month'] = rows.find_element_by_xpath('.//td[16]').text

                            item['vaccinate'] = rows.find_element_by_xpath('.//td[17]').text

                            item['dr_name'] = rows.find_element_by_xpath('.//td[18]').text

                            item['scraped_time'] = datetime.now().strftime('%m/%d/%Y')
                            item['platform'] = 'http://www.mcgm.gov.in/irj/portal/anonymous/qldoglican?guest_user=english'

                        except:
                            pass
                        finally:
                            yield item
                    try:
                        next_record = driver.find_element_by_id('WDBE-btn-3')
                        next_record.click()
                        time.sleep(2)
                    except:
                        break
                except Exception as e:
                    break
        except Exception as exc:
            print(exc)
        time.sleep(1)
        driver.quit()

