from transformers import pipeline

pipe = pipeline("audio-classification", model="dima806/bird_sounds_classification")

result = pipe("path/to/audio/file.mp3")

print(result[0])