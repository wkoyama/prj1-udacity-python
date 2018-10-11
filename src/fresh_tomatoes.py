# -*- coding: utf-8 -*-
import webbrowser
import os
import re
import sys
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>Filmes populares do momento!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet"
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="../css/movie-content.css">
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    {movie_overlay_content}
    <!-- Main Page Content -->
    <nav class="navbar navbar-dark navbar-expand-lg bg-dark" role="navigation">
        <div class="container">
            <div class="navbar-header">
            <a class="navbar-brand" href="#">Filmes Populares do momento</a>
            </div>
        </div>
    </nav>

    <div class="container">
      {movie_tiles}
    </div>

    <script
    src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    crossorigin="anonymous">
    </script>
    <script
    src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
    integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
    crossorigin="anonymous">
    </script>
    <script
    src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js">
    </script>
    <script src="../js/movie-content.js"></script>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center float-left pt-5"
onclick="openMovieContent({movie_id})"
data-movie-id="{movie_id}"
data-trailer-youtube-id="{trailer_youtube_id}"
data-toggle="overlay"
data-target="#movie-content-{movie_id}">
    <img src="{poster_image_url}" width="220" height="342">
    <h2 class="pt-3">{movie_title}</h2>
</div>
'''

# A single overlay movie entry
movie_tile_overlay_content = '''
<!-- The overlay -->
    <div id="movie-content-{movie_id}" class="overlay" aria-hidden="true">

        <!-- Button to close the overlay navigation -->
        <a href="javascript:void(0)"
        class="closebtn hanging-close"
        data-dismiss="overlay"
        onclick="closeMovieContent({movie_id})">&times;</a>

        <!-- Overlay content -->
        <div class="overlay-content overlay-font">
            <div class="container-fluid">
                <div class="container">
                    <div class="row justify-content-md-center">
                        <div class="col-sm">
                            <div class="poster">
                                <img src="{poster_image_url}"
                                width="220"
                                height="342">
                            </div>
                        </div>
                        <div class="col-md-9 movie-content mt-1">
                            <div class="movie-title pb-3">
                                <span>
                                    {movie_title}
                                </span>
                            </div>
                            <div class="movie-description pb-3">
                                <span>
                                    {movie_description}
                                </span>
                            </div>
                            <div class="movie-info">
                                <label>Data de Lançamento:</label>
                                <span>{movie_release_date}</span>
                            </div>

                            <div class="movie-info">
                                <label>Media de Votos:</label>
                                <span>{movie_vote_average}</span>
                            </div>
                            <div class="movie-info">
                                <label>Quantidade de votos:</label>
                                <span>{movie_vote_count}</span>
                            </div>
                            <div class="movie-info">
                                {movie_genre}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="row mt-4 border-bottom">
                        <div class="movie-trailer-desc">
                            <span class="movie-subtitle">Trailer</span>
                        </div>
                    </div>
                    <div class="row mt-5 justify-content-md-center">
                        <div class="col-12 col-md-8">
                            <div class="movie-trailer"
                            data-movie-id="{movie_id}">
                                <div
                                class="embed-responsive embed-responsive-16by9"
                                id="trailer-video-container-{movie_id}">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
'''

# A single genre badge
movie_tile_genre = '''
    <span class="badge badge-secondary mr-2">{genre_description}</span>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        if movie.trailer_url:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_url)
        else:
            youtube_id_match = None

        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        if(trailer_youtube_id):
            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                movie_title=movie.title,
                poster_image_url=movie.image,
                trailer_youtube_id=trailer_youtube_id,
                movie_id=movie.id
            )
    return content


def create_movie_overlay_content(movies):
    # The HTML content for overlay movie
    content = ''
    for movie in movies:
        if movie.trailer_url:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_url)
        else:
            youtube_id_match = None

        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        if(trailer_youtube_id):
            data = datetime.strptime(movie.release_date, '%Y-%m-%d')
            data = data.strftime('%d/%m/%Y')

            genre_content = ''
            for genre in movie.genres:
                genre_content +=
                movie_tile_genre.format(genre_description=genre)

            # Append the tile with its content to render
            content += movie_tile_overlay_content.format(
                movie_title=movie.title,
                movie_description=movie.description,
                movie_popularity=movie.popularity,
                movie_vote_average=movie.vote_average,
                movie_vote_count=movie.vote_count,
                poster_image_url=movie.image,
                trailer_youtube_id=trailer_youtube_id,
                movie_id=movie.id,
                movie_release_date=data,
                movie_genre=genre_content
            )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('./pages/fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    overlay = create_movie_overlay_content(movies).encode("utf-8")
    rendered_content = main_page_content.format(
        movie_overlay_content=overlay,
        movie_tiles=create_movie_tiles_content(movies).encode("utf-8"))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
