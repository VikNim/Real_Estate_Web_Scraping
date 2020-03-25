from selenium import webdriver
import time
import csv

try:
    store_file = open('Sites.csv', 'a')
    field_names = ['Sites']
    writer = csv.DictWriter(store_file, fieldnames=field_names)
    writer.writeheader()
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    time.sleep(2)
    driver.implicitly_wait(10)

    input_no = driver.find_element_by_id('ctl00_Contentplaceholder2_ctl02_txtAccno')
    input_no.send_keys('site:parset.com')

    while True:
        try:
            driver.implicitly_wait(60)
            sites = driver.find_elements_by_xpath('')

            for site in sites:
                site_name = site.find_element_by_xpath('').__getattribute__('onclick')
                writer.writerow({'Sites': ''})
            button = driver.find_element_by_id('ctl00_Contentplaceholder2_ctl02_btnGo')
            button.click()
            driver.implicitly_wait(60)
            time.sleep(2)

        except Exception as ex:
            break

    time.sleep(2)
    driver.quit()
except Exception as ex:
    print(ex)
