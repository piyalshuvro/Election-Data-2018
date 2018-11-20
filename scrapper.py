from selenium import webdriver;
from selenium.webdriver.support.ui import Select;
import time;
from bs4 import BeautifulSoup
import pandas as pd

#initialize counter to be used for saving the files
x = 0

global zillaStart
global panchayetStart
#initialize driver and get the website link
driver = webdriver.Chrome()
driver.get("http://www.wbsec.org/PublicPages/VotingResult2018.aspx")

# select candidate field for gram panchayet

candidateSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbCandidateFor'))
candidateOption = candidateSelect.options
candidateSelect.select_by_index(3)

# zilla parishad select

zillaParishadSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbZillaParisadName'))
zillaParishadOption = zillaParishadSelect.options
zillaParishadSelect.select_by_index(1)
time.sleep(5)
zillaStart = 19

for zillaParishadValue in range(zillaStart, len(zillaParishadOption)):
    zillaParishadSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbZillaParisadName'))
    zillaParishadOption = zillaParishadSelect.options

    zillaParishadSelect.select_by_index(zillaParishadValue)
    time.sleep(5)
    zillaParishadSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbZillaParisadName'))
    zillaParishadOption = zillaParishadSelect.options

    #save the zilla parishad name
    zillaParishadName = zillaParishadOption[zillaParishadValue].text
    print("District Value: " + str(zillaParishadValue))

    # panchayet samity select

    panchayatSamitySelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbPanchayatSamity'))
    panchayatSamityOption = panchayatSamitySelect.options

    if(zillaParishadValue == zillaStart):
        panchayetStart = 13
    else:
        panchayetStart = 1


    for panchayatSamityValue in range(panchayetStart, len(panchayatSamityOption)):
        panchayatSamitySelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbPanchayatSamity'))

        panchayatSamitySelect.select_by_index(panchayatSamityValue)
        panchayatSamityOption = panchayatSamitySelect.options

        # save panchayet samity name
        panchayatSamityName = panchayatSamityOption[panchayatSamityValue].text
        print("Panchayet Value: " + str(panchayatSamityValue))

        time.sleep(2)

        # GP select
        gpSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbGramPanchayat'))
        gpOption = gpSelect.options


        for gpValue in range(1, len(gpOption)):
            gpSelect = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$cmbGramPanchayat'))
            gpSelect.select_by_index(gpValue)
            gpOption = gpSelect.options


            # save Gp Name
            gpName = gpOption[gpValue].text
            time.sleep(2)

            # click on search button
            searchButton = driver.find_element_by_id('ContentPlaceHolder1_btnSearch')
            searchButton.click()

            time.sleep(2)

            # handover the webpage to beautiful soup to extract the table
            soup = BeautifulSoup(driver.page_source, 'lxml')

            # get the table content from the webpage
            table = soup.find_all('table')

            # save the table temporarily
            for rows in table:
                with open("C:\Monash RA Work\Election 2018\Temp Data\data_%s.xls" % x, 'w') as myfile:
                    myfile.write(str(rows))


            # convert the table to data frame and save to hard disk
            name = zillaParishadName.strip().replace("\n", "") + "_" + panchayatSamityName.strip().replace("\n", "") +"_" + gpName.strip().replace("\n", "")
            for i, df in enumerate(pd.read_html("C:\Monash RA Work\Election 2018\Temp Data\data_%s.xls" % x)):
                df.to_csv("C:\Monash RA Work\Election 2018\Final Data\%s.csv" % name, index=False, encoding='utf-8')


            # increment counter used in saving the table data for temporary purpose
            x=x+1
            time.sleep(2)



















