import webbrowser

class Movie():
    
    """This is a class that initializes 4 attributes and contains one function.
    
    Attributes:
    
    title(str): It is the movie title.
    storyline(str): It is the movie summary.
    poster_image_url(str): It is the URL of movie poster.
    trailer_youtube_url(str): It is the URL of the movie's trailer.
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube

    #Function written to open trailer in webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
