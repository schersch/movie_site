import webbrowser


class Movie():
    """Movie class, contains information about a particular movie.

    Attributes:
        title: title of the movie
        year: year the movie was released
        storyline: a summary of the movie storyline
        image: a link to a jpg image of the movie poster
        trailer: a youtube link to the movie trailer
    """
    
    def __init__(self, title, year, storyline, image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
