from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common. by import By
from selenium.webdriver.common.keys import Keys
import time

web_URL="https://appbrewery.github.io/Zillow-Clone/"
google_form="https://docs.google.com/forms/d/e/1FAIpQLSexrc3y8TQFlUZ6C1OdaNFF1WoqM-ACr-HfaH8dUsgi4Cw9_g/viewform?usp=header"

response= requests.get(web_URL)

data=response.text

soup = BeautifulSoup(response.content, 'html.parser')
links=soup.select(".StyledPropertyCardDataWrapper a")

all_links=[link["href"] for link in links]

price_elements=soup.select(".PropertyCardWrapper__StyledPriceLine")
prices=[price.get_text().replace("/mo","").split("+")[0] for price in price_elements]

# print(prices)

address_elements=soup.select(".StyledPropertyCardDataWrapper address")
all_adresses=[each_address.get_text().replace(" | "," ").strip() for each_address in address_elements]
# print(all_adresses)

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)

for n in range(10):

        driver.get(google_form)
        time.sleep(2)

        address_fill=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_fill.send_keys(all_adresses[n])

        price_fill=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_fill.send_keys(prices[n])
        time.sleep(2)

        link_fill=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_fill.send_keys(all_links[n],Keys.ENTER)

        submit_btn=driver.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
        submit_btn.click()
