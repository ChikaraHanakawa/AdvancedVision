import requests
import time
from bs4 import BeautifulSoup
from transformers import pipeline
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pipe = pipeline("audio-classification", model="dima806/bird_sounds_classification")

result = pipe("/home/chikara/Downloads/crow.mp3")

print(result[0]['label'])

serch_word = result[0]['label']
serch_word = serch_word.replace(' ', '')
const = 'https://search.yahoo.co.jp/image/search?p='
url = const + serch_word

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

image_tags = driver.find_elements(By.TAG_NAME, 'img')
image_tag = image_tags[0]

with open('serch_result.jpg', 'wb') as f:
    f.write(requests.get(image_tag.get_attribute('src')).content)
    print('Downloaded image')

driver.quit()