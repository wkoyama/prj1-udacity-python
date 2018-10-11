import webbrowser
from integration_apis import MovieDB


class Media():
    def __init__(self, id, title, description, image, release_date):
        self.id = id
        self.title = title
        self.description = description
        self.image = "https://image.tmdb.org/t/p/w500" + image
        self.release_date = release_date


class Movie(Media):
    """ Acessando a documentacao de Movie """
    def __init__(self, item):
        id = item['id']
        title = item['title']
        overview = item['overview']
        poster = item['poster_path']
        release_date = item['release_date']
        Media.__init__(self, id, title, overview, poster, release_date)
        self.vote_average = item['vote_average']
        self.vote_count = item['vote_count']
        self.popularity = item['popularity']
        self.genres = MovieDB().get_genre_info(item['genre_ids'])
        self.videos = MovieDB().get_videos(item['id'])

        if (len(self.videos['results']) == 0):
            url = None
        else:
            url = self.videos['results'][0]

        self.trailer_url = self.build_url(url)

    def show_trailer(self):
        url = self.trailer_url

        if(url is None):
            return

        webbrowser.open(url)

    def build_url(self, item):
        if(item is None):
            return None

        if(item['site'] == "YouTube"):
            return MovieDB().get_youtube_video(item)

        return None
