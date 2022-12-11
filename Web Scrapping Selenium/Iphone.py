#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time




driver=webdriver.Chrome("chromedriver_win32")




driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")




rating=[]
review_summary=[]
full_review=[]




rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
for i in rating_tags[0:10]:
    ratingr=i.text
    rating.append(ratingr)
    
review_summary_tag=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
for i in review_summary_tag[0:10]:
    review_summaryy=i.text
    review_summary.append(review_summaryy)
    
full_review_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
for i in full_review_tags[0:10]:
    fullr=i.text
    full_review.append(fullr)




print(len(rating),len(review_summary),len(full_review))




rating




review_summary




full_review



rating1=[]
review_summary1=[]
full_review1=[]




start=0
end=2
for page in range(start,end):
    rating_tags1=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tags1:
        rating1.append(i.text)
    review_summary_tag1=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in review_summary_tag1:
        review_summary1.append(i.text)
    full_review_tags1=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_review_tags1:
        full_review1.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(3)




print(len(rating1),len(review_summary1),len(full_review1))





rating1




review_summary1




full_review1




rating2=[]
review_summary2=[]
full_review2=[]





for page in range(1,10):
    rating_tags2=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tags2:
        rating2.append(i.text)
    review_summary_tag2=driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
    for i in review_summary_tag2:
        review_summary2.append(i.text)
    full_review_tags2=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
    for i in full_review_tags2:
        full_review2.append(i.text)
    next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
    next_button.click()
    time.sleep(6)


# In[ ]:




