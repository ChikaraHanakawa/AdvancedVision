'''
Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License.
'''
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from model import Model

class App:
    def __init__(self, sound_file_path):
        self.model = Model()
        self.conf = self.model.ReadConfig()
        self.conf['model']['sound_path'] = sound_file_path
        self.model.SoundToImage(self.conf['model']['sound_path'], self.conf['model']['image_url'])
        self.url = self.model.get_url()
    
    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(self.url)
        bird_name = self.model.serch_word
        bird_name = bird_name.replace('-', ' ')
        
        image_tags = driver.find_elements(By.TAG_NAME, 'img')
        for i in range(len(image_tags)):
            image_tag = image_tags[i]
            if bird_name.lower() in image_tag.get_attribute('alt').lower() or bird_name.lower() in image_tag.get_attribute('title').lower():
                with open(self.conf['app']['save_path'], 'wb') as f:
                    f.write(requests.get(image_tag.get_attribute('src')).content)
                    print('Downloaded image')
                break
        driver.quit()
    
def main():
    app = App()
    app.run()

if __name__ == '__main__':
    main()