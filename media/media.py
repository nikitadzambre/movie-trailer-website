import webbrowser


class Movie():

    """The Movie class defines the attributes of a movie
    Attributes:
        title (str): Name of the movie.
        storyline (str): Summary of the movie.
        poster_image_url (str): URL of the poster image of the movie.
        trailer_youtube_url (str): Youtube URL of the official trailer of the
                                   movie
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):

        """Opens the trailer of a movie"""

        webbrowser.open(self.trailer_youtube_url)
