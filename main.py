from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #check if page is loaded and ready
from selenium.webdriver.support import expected_conditions as EC
import time
from loginToCodeforces import login
from csvFileAccess import generateNamesFromCsvFile
import math
import csv



driver = webdriver.Chrome()

driver.get("https://codeforces.com/group/rZXLOcYbKV/contest/312716/standings/groupmates/true/page/1")
time.sleep(2)
pagesToCheck = ["https://codeforces.com/group/rZXLOcYbKV/contest/312716/standings/groupmates/true/page/1",
                "https://codeforces.com/group/rZXLOcYbKV/contest/312716/standings/groupmates/true/page/2",
                "https://codeforces.com/group/rZXLOcYbKV/contest/312716/standings/groupmates/true/page/3",
                "https://codeforces.com/group/rZXLOcYbKV/contest/312716/standings/groupmates/true/page/4",
                "https://codeforces.com/group/rZXLOcYbKV/contest/312716/standings/groupmates/true/page/5"]

login("", "", driver)   #enter a valid codeforces username (handle) and password as first and second parameters to the login function
time.sleep(4)
namesToRemove = generateNamesFromCsvFile()
namesFoundAndRemoved = []
namesFoundButHadAlreadyBeenRemoved = []
namesNotFoundAtAll = []


for i in namesToRemove: 
    print(i)

for cheater in namesToRemove:
    #need to search for the cheater in all pages
    found = False
    removedToPractice = False

    for i in range(0, len(pagesToCheck)):
        driver.get(pagesToCheck[i])
        time.sleep(3)
        xPathName = "/profile/" + cheater
        fullXPath = '//a[@href="' + xPathName + '"]'
        #print('//a[@href="' + xPathName + '"]')
        #print('//a[@href="/profile/WrongAnswer214"]')
        #print(xPathName)
        try:
            driver.find_element_by_xpath('//a[@href="' + xPathName + '"]')
            found = True
        except:
            print(cheater + " wasnt found in this page, will continue searching")
            continue

        print("Found " + cheater)

        try:
            toPractice = driver.find_element_by_xpath(fullXPath + '/following-sibling::a')
            toPractice.click()
            time.sleep(3)
            clickButton = driver.find_elements_by_name("codeforces-dialog-ok-button")
            clickButton.click()
            time.sleep(3)
            removedToPractice = True
            break   #completely done with this cheater so will break to go on to the next cheater
        except:
            print(cheater + " already removed")
            continue
    if (found and removedToPractice):
        namesFoundAndRemoved.append(cheater)
    elif (not found):
        namesNotFoundAtAll.append(cheater)
    elif (found and not removedToPractice):
        namesFoundButHadAlreadyBeenRemoved.append(cheater)


print("\n\n\nNames of all cheaters found and removed")
for i in namesFoundAndRemoved:
    print(i)


print("\n\nNames of all cheaters found but had already been removed")
for i in namesFoundButHadAlreadyBeenRemoved:
    print(i)

print("\n\nNames of cheaters not found at all")
for i in namesNotFoundAtAll:
    print(i)        



#<a href="/profile/WrongAnswer214" title="Expert WrongAnswer214" class="rated-user user-blue">WrongAnswer214</a>
#<input class="ok" name="codeforces-dialog-ok-button" type="button" value="OK">