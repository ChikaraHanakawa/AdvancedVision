import requests
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from model import Model

class App:
    def __init__(self):
        self.model = Model()
        self.conf = self.model.ReadConfig()
        self.model.SoundToImage(self.conf['model']['sound_path'], self.conf['model']['image_url'])
        self.url = self.model.get_url()
    
    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(self.url)
        image_tags = driver.find_elements(By.TAG_NAME, 'img')
        image_tag = image_tags[0]
        with open(self.conf['app']['save_path'], 'wb') as f:
            f.write(requests.get(image_tag.get_attribute('src')).content)
            print('Downloaded image')
        driver.quit()
    
def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()