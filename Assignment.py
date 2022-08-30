from selenium import webdriver
import time
import csv
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:\\Users\\Hitesh\\Downloads\\chromedriver_win32\\chromedriver.exe")

foodlist = ['brown-rice-cooked', 'Paneer' , 'Tofu']
templist = []
r = 1


for i in foodlist:
    driver.get('https://www.nutritionix.com/food/${foodlist[i]}')
    driver.implicitly_wait(5)

    while(1):
        try:
            method = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div['+str(r)+']/strong').text
            pValue = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/div/div/div/div['+str(r)+']/div/strong').text
            Table_dict = {
                'Method':method,
                'Description':pValue
            }
            templist.append(Table_dict)
            df = pd.DataFrame(templist)
            r += 1

        except NoSuchElementException:
            break

    df.to_csv('table.csv') 

    calories = driver.find_element_by_class_name('box-content ng-binding')
    print(calories.data.protein)
    print(calories.data.total_carbohydrate)
    print(calories.data.total_fat)   
