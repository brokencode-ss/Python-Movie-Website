import fresh_tomatoes
import media

# A collection of some of my favourite films
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

tumbbad = media.Movie(
    "Tumbbad",
    "A mythological tale of a greedy man and a demonic treasure.",
    "https://upload.wikimedia.org/wikipedia/en/4/41/Tumbbad_poster.jpg",
    "https://www.youtube.com/watch?v=sN75MPxgvX8")

ratatouille = media.Movie(
    "Ratatouille",
    "A rat becomes a chef.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=NgsQ8mVkN8w")

seven = media.Movie(
    "Seven",
    "A man targets people to kill who commit the seven sins.",    
    "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=znmZoVkCjpI")

satya = media.Movie(
    "Satya",
    "A common man's journey to become an underworld goon.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/52/Satya_%281998%29.jpg/220px-Satya_%281998%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=CJlrrBZAatM")

ugly = media.Movie(
    "Ugly",
    "A man's daughter goes missing from his car.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/61/Movie_Poster_Ugly.jpg/220px-Movie_Poster_Ugly.jpg",  # NOQA
    "https://www.youtube.com/watch?v=4ougQY2-zpk")

# Array that stores the names of all the instances created.
movies = [toy_story, tumbbad, ratatouille, seven, satya, ugly]

# Function call for opening the movie website.

fresh_tomatoes.open_movies_page(movies)


