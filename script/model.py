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