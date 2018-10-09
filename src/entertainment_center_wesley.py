import fresh_tomatoes
import media
from integration_apis import MovieDB

movies = []
populares = MovieDB().get_popular()

for pop in populares['results']:
    movie = media.Movie(pop)
    movies.append(movie)

fresh_tomatoes.open_movies_page(movies)
