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

    def get_genres(self):
        url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-BR&" + self.get_key()
        payload = "{}"
        response = requests.request("GET", url, data=payload)
        
        all_genres = json.loads(response.text)['genres']

        genres_description = {}

        for genre in all_genres:
            current = genre['id']
            description = genre['name']
            genres_description[current] = description

        return genres_description
    
    def get_genre_info(self, genres):
        genres_description = self.get_genres()

        arrReturn = []
        for key in genres:
            arrReturn.append(genres_description[key])    

        return arrReturn
#MovieDB().get_popular()
