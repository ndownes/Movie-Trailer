import webbrowser

# Defines class Movie and sets out the common categories of information for each instance of the class
class Movie():
    def __init__(self, movie_title, movie_year, movie_rating, movie_review, movie_reviewer, poster_image, trailer_youtube):
        self.title = movie_title
        self.year = movie_year
        self.rating = movie_rating
        self.review = movie_review
        self.reviewer = movie_reviewer
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
