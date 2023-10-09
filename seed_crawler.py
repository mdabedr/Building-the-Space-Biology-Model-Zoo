# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import random
import numpy as np

pages=[]

import random
for i in range(150):
    x = random.randint(0,300)
    pages.append(x)

osd_title = []
osd_description = []
osd_factor = []
osd_organism=[]
osd_assays1=[]
osd_assays2=[]
osd_assays3=[]

all_data=[]
for page in pages:
    time.sleep(random.randint(1, 10))

    urlpage = 'https://osdr.nasa.gov/bio/repo/data/studies/OSD-' + str(page)
    driver = webdriver.Firefox(executable_path = 'C:/Users/Asus/Downloads/geckodriver.exe')
    # get web page
    driver.get(urlpage)
    # execute script to scroll down the page
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    # sleep for 30s
    time.sleep(30)
    ###for description
    results=driver.find_elements_by_xpath("//*[@class='ws-pre-line']")
    print('Number of results', len(results))
    for result in results:
        temp_des="<description> "+result.text+" </description>"
        osd_description.append(temp_des)
    all_data.append(temp_des)
    ##for factors
    results_factor = driver.find_elements_by_xpath("//*[@class='mat-cell cdk-cell cdk-column-concept mat-column-concept ng-star-inserted']//*[@class='ng-star-inserted']")
    print('Number of results', len(results_factor))
    tmp_factor=[]

    for result in results_factor:
        tmp_factor.append(result.text)
    joined_fac=''.join(tmp_factor)
    temp_fac="<factor> "+joined_fac+" </factor>"
    osd_factor.append(temp_fac)
    all_data.append(temp_fac)

    ###for organism
    results_organism = driver.find_elements_by_xpath("//*[@class='mat-grid-tile-content']")
    print('Number of organism', len(results_organism))
    tmp_organism=[]
    for result in results_organism:
        tmp_organism.append(result.text)
    tmp_org="<organism> " + ''.join(tmp_organism) + " </organism>"
    osd_organism.append(tmp_org)
    all_data.append(tmp_org)

    ###for title
    results_title = driver.find_elements_by_xpath("//*[@class='three-quarters-width']//*[@class='ng-star-inserted']")
    print('Number of title', len(results_title))
    tmp_title = []
    for result in results_title:
        tmp_title.append(result.text)
    tmp_tit = "<title> " + ''.join(tmp_title) + " </title>"
    osd_title.append(tmp_tit)
    all_data.append(tmp_tit)

    ##for assays
    results_assays1 = driver.find_elements_by_xpath("//*[@class='mat-cell cdk-cell cdk-column-measurement mat-column-measurement ng-star-inserted']//*[@class='ng-star-inserted']")
    results_assays2 = driver.find_elements_by_xpath("//*[@class='mat-cell cdk-cell cdk-column-technology mat-column-technology ng-star-inserted']//*[@class='ng-star-inserted']")
    results_assays3 = driver.find_elements_by_xpath("//*[@class='mat-cell cdk-cell cdk-column-platform mat-column-platform ng-star-inserted']")

    tmp_assay1 = []
    tmp_assay2 = []
    tmp_assay3 = []

    for result in results_assays1:
        tmp_assay1.append(result.text)
    joined_ass1=''.join(tmp_assay1)
    tmp_ass1 = "<measurement> " + joined_ass1 + " </measurement>"
    osd_assays1.append(tmp_ass1)
    for result in results_assays2:
        tmp_assay2.append(result.text)
    joined_ass2 = ''.join(tmp_assay2)
    tmp_ass2 = "<technology> " + joined_ass2 + " </technology>"
    osd_assays2.append(tmp_ass2)
    for result in results_assays3:
        tmp_assay3.append(result.text)
    joined_ass3 = ''.join(tmp_assay3)
    tmp_ass3 = "<device> " + joined_ass3 + " </device>"
    osd_assays3.append(tmp_ass3)

    all_data.append(tmp_ass1)
    all_data.append(tmp_ass2)
    all_data.append(tmp_ass3)

    driver.close()


pd.DataFrame(all_data).to_csv("all_data.csv", index=False)

pd.DataFrame(osd_title).to_csv("title.csv", index=False)
pd.DataFrame(osd_description).to_csv("description.csv", index=False)
pd.DataFrame(osd_factor).to_csv("factor.csv", index=False)
pd.DataFrame(osd_organism).to_csv("organism.csv", index=False)
pd.DataFrame(osd_assays1).to_csv("assays1.csv", index=False)
pd.DataFrame(osd_assays2).to_csv("assays2.csv", index=False)
pd.DataFrame(osd_assays3).to_csv("assays3.csv", index=False)
