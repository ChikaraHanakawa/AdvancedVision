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
import yaml
from transformers import pipeline

class Model:
    def __init__(self) -> None:
        self.url = None
        self.pipe = pipeline("audio-classification", model="dima806/bird_sounds_classification")
        self.result = None
    
    def SoundToImage(self, sound_path, url):
        self.result = self.pipe(sound_path)
        print(self.result[0])
        self.serch_word = self.result[0]['label']
        replace_serch_word = self.serch_word.replace(' ', '')
        self.const = url
        self.url = self.const + replace_serch_word
    
    def ReadConfig(self):
        with open('config/config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        return config

    def get_url(self):
        return self.url