from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()

store_file = open('Sample.csv', 'w')
field_names = ['Ward', 'Valid From', 'Valid To', 'House No', 'House Name', 'Street No', 'Area', 'Area1', 'Postal Code',
               'Telephone No', 'Dog Name', 'Gender', 'Dog Breed', 'Age In Month', 'Age In Month', 'Vaccination Data',
               'Doctor Name']
writer = csv.DictWriter(store_file, fieldnames=field_names)
writer.writeheader()

driver.get('http://www.mcgm.gov.in/irj/portal/anonymous/qldoglican?guest_user=english')
time.sleep(5)
driver.implicitly_wait(5)

try:
    driver.switch_to.frame(driver.find_element_by_id('ivuFrm_page0ivu0'))
    time.sleep(3)
    driver.implicitly_wait(5)

    # print('In First Frame')

    # print(driver.page_source)

    frame = driver.find_element_by_xpath('//frameset[1]/frame[1]')
    # print(frame.get_attribute('src'))

    driver.switch_to.frame(driver.find_element_by_xpath('//frameset[1]/frame[1]'))
    time.sleep(3)
    driver.implicitly_wait(5)
    # print('In Second Frame')

    # print(driver.page_source)

    first_ward_no = driver.find_element_by_id('WD1C')
    first_ward_no.clear()
    first_ward_no.send_keys('50000226')

    second_ward_no = driver.find_element_by_id('WD20')
    second_ward_no.clear()
    second_ward_no.send_keys('50000227')

    search_records = driver.find_element_by_id('WD5B')
    search_records.click()
    time.sleep(5)
    c = 1

    while(1):
        if c == 2:
            break
        c = c + 1
        try:
            table_rows = driver.find_elements_by_xpath('//td[@id="WD62-content"]/table/tbody/tr')
            # table_rows2 = driver.find_element_by_xpath('//td[@id="WD62-content"]/table/tbody/tr[5]/td[3]')
            # print(table_rows2.text)

            for rows in table_rows[1:]:
                try:
                    ward = rows.find_element_by_xpath('.//td[2]/span').text
                    # print(ward)

                    valid_from = rows.find_element_by_xpath('.//td[3]').text
                    print(valid_from)
                    valid_to = rows.find_element_by_xpath('.//td[4]').text
                    print(valid_to)
                    house_no = rows.find_element_by_xpath('.//td[5]').text
                    # print(house_no)
                    house_name = rows.find_element_by_xpath('.//td[6]').text
                    # print(house_name)
                    street_no = rows.find_element_by_xpath('.//td[7]').text
                    # print(street_no)
                    area = rows.find_element_by_xpath('.//td[8]').text

                    area1 = rows.find_element_by_xpath('.//td[9]').text
                    postal_code = rows.find_element_by_xpath('.//td[10]').text
                    tele_no = rows.find_element_by_xpath('.//td[11]').text
                    dog_name = rows.find_element_by_xpath('.//td[12]').text
                    print(dog_name)
                    gender = rows.find_element_by_xpath('.//td[13]').text
                    breed = rows.find_element_by_xpath('.//td[14]').text
                    print(breed)
                    age_year = rows.find_element_by_xpath('.//td[15]').text
                    age_month = rows.find_element_by_xpath('.//td[16]').text
                    vaccinate = rows.find_element_by_xpath('.//td[17]').text
                    dr_name = rows.find_element_by_xpath('.//td[18]').text
                    # print(dr_name)

                    writer.writerow({'Ward': ward, 'Valid From': valid_from, 'Valid To': valid_to, 'House No': house_no,
                                     'House Name': house_name, 'Street No': street_no, 'Area': area, 'Area1': area1,
                                     'Postal Code': postal_code, 'Telephone No': tele_no, 'Dog Name': dog_name,
                                     'Gender': gender, 'Dog Breed': breed, 'Age In Year': age_year,
                                     'Age In Month': age_month, 'Vaccination Data': vaccinate, 'Doctor Name': dr_name})
                except:
                    pass
            try:
                next_record = driver.find_element_by_id('WDBE-btn-3')
                next_record.click()
                time.sleep(2)
            except:
                store_file.close()
                break
        except Exception as e:
            store_file.close()
            break


except Exception as exc:
    store_file.close()
    print(exc)
store_file.close()
time.sleep(1)
driver.quit()
