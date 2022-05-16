from selenium import webdriver

driver = webdriver.Chrome('/Users/steven/chromedriver')
URL = 'https://www.google.com/search?q=bitcoin&tbm=nws'
driver.get(URL)

headlines = []
list1 = [headline_1, headline_2, headline_3]

# /html/body/div[7]/div[2]/div[8]/div[2]/div/div[2]/div[2]/div/div/div[1]/g-card/div/div/div[2]/a/div/div[2]/div[2]
headline_1 = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/g-card/div/div/div[2]/a/div/div[2]/div[2]').get_attribute('innerHTML')
headline_2 = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/g-card/div/div/div[2]/a/div/div[2]/div[2]').get_attribute('innerHTML')
headline_3 = driver.find_element_by_xpath('//*[@id="rso"]/div[3]/g-card/div/div/div[2]/a/div/div[2]/div[2]').get_attribute('innerHTML')
######## the first dive in the xpath contains the newsnumber
#works untill div[10], for >10 we need to go to the next page.

i=0
while i < 3:
    headlines.append(list1[i])
    i+=1
# change loop, also try to use the xpath div nr as a variable and run that from 1 to 10
# also, check if next page div starts at 11 or at 1

headlines

headline_1
headline_2
headline_3
