from selenium import webdriver;
from selenium.webdriver.support.ui import Select;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.common.by import By;
from selenium.common.exceptions import NoSuchElementException
import time;
import os
import glob
import shutil
from bs4 import BeautifulSoup
import pandas as pd


import os

x = 0
driver = webdriver.Chrome()
driver.get("http://www.wbsec.org/PublicPages/VotingResult2018.aspx")

# first loop for candidate


candidateSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbCandidateFor'))
candidateOption = candidateSelect.options
candidateSelect.select_by_index(3)

# zilla parishad select

zillaParishadSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbZillaParisadName'))
zillaParishadOption = zillaParishadSelect.options

for zillaParishadValue in range(1, len(zillaParishadOption)):
for zillaParishadValue in range(12, len(zillaParishadOption)):
    zillaParishadSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbZillaParisadName'))
    zillaParishadOption = zillaParishadSelect.options

    zillaParishadSelect.select_by_index(zillaParishadValue)
    zillaParishadName = zillaParishadOption[zillaParishadValue].text

    time.sleep(5)

    panchayatSamitySelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbPanchayatSamity'))
    panchayatSamityOption = panchayatSamitySelect.options


    for panchayatSamityValue in range(1, len(panchayatSamityOption)):
    for panchayatSamityValue in range(11, len(panchayatSamityOption)):
        panchayatSamitySelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbPanchayatSamity'))

        panchayatSamitySelect.select_by_index(panchayatSamityValue)
        panchayatSamityOption = panchayatSamitySelect.options
        panchayatSamityName = panchayatSamityOption[panchayatSamityValue].text

        time.sleep(2)

        gpSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbGramPanchayat'))
        gpOption = gpSelect.options
        print("Gp Length: " + str(len(gpOption)))

        for gpValue in range(1, len(gpOption)):
            gpSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbGramPanchayat'))
            gpSelect.select_by_index(gpValue)
            gpOption = gpSelect.options
            gpName = gpOption[gpValue].text
            time.sleep(2)





            searchButton = driver.find_element_by_id('ContentPlaceHolder1_btnSearch')
            searchButton.click()

            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            datalist = []

            table = soup.find_all('table')





            for rows in table:
                with open("data_%s.xls" % x, 'w') as myfile:
                with open("C:\Monash RA Work\Election 2018\Temp Data\data_%s.xls" % x, 'w') as myfile:
                    myfile.write(str(rows))



            name = zillaParishadName + "_" + panchayatSamityName +"_" + gpName
            for i, df in enumerate(pd.read_html("data_%s.xls" % x)):
                df.to_csv("%s.csv" % name, index=False, encoding='utf-8')
            for i, df in enumerate(pd.read_html("C:\Monash RA Work\Election 2018\Temp Data\data_%s.xls" % x)):
                df.to_csv("C:\Monash RA Work\Election 2018\Final Data\%s.csv" % name, index=False, encoding='utf-8')

            x=x+1
            time.sleep(2)
            #
            # df.to_csv("")


















