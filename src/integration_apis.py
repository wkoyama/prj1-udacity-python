import requests
import json

class MovieDB():

    def __init__(self):
        self.API_KEY = "6346f2fccfe152d1e521b16b34ee607c"
        self.AUTH_TOKEN = "eyJhdWQiOiI2MzQ2ZjJmY2NmZTE1MmQxZTUyMWIxNmIzNGVlNjA3YyIsInN1YiI6IjViYjU4MDE5YzNhMzY4MTUwYzAwNWIxNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MMVA7pKzeCpBybkhGvJN0LhIR9QiNsyt8IdyLwSttDo"

    def get_key(self):
        return "api_key=" + self.API_KEY
    
    def get_popular(self):
        url = "https://api.themoviedb.org/3/movie/popular?language=pt-BR&page=1&" + self.get_key()
        payload = "{}"
        response = requests.request("GET", url, data=payload)
        return json.loads(response.text)

    def get_videos(self, movie_id):
        url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/videos?language=pt-BR&page=1&" + self.get_key()
        payload = "{}"
        response = requests.request("GET", url, data=payload)
        return json.loads(response.text)

    def get_youtube_video(self, item):
        url = "https://www.youtube.com/watch?v=" + item['key']
        return url
        
#MovieDB().get_popular()
