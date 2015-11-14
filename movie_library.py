import movies
import fresh_tomatoes


#Building a list of movies to be displayed on a web page
pi = movies.Movie(
    "Pi","1998", "A mathemetician finds truth in chaos.",
    "https://www.movieposter.com/posters/archive/main/68/MPW-34133",
    "https://www.youtube.com/watch?v=jo18VIoR2xU")
shawshank_redemption = movies.Movie(
    "The Shawshank Redemption","1994",
    "An innocent man endures prison life and finds redemption.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
thank_you_for_smoking = movies.Movie(
    "Thank You For Smoking","2005",
    "Fast talker faces assasination attempts.",
    "https://upload.wikimedia.org/wikipedia/en/c/c3/Thank_you_for_smoking_Poster.jpg",
    "https://www.youtube.com/watch?v=s3eeTjK0qZY")
garden_state = movies.Movie(
    "Garden State","2004","Depressed man returns home and finds himself.",
    "https://upload.wikimedia.org/wikipedia/en/3/3c/Garden_State_Poster.jpg",
    "https://www.youtube.com/watch?v=6ZbqE23IRH0")
fifth_element = movies.Movie(
    "The Fifth Element","1997",
    "To save the world, a man must save the ultimate weapon",
    "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
    "https://www.youtube.com/watch?v=VkX7dHjL-aY")
dark_knight = movies.Movie(
    "The Dark Knight","2008",
    "Batman faces his greatest adversary.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=kmJLuwP3MbY")
se7en = movies.Movie(
    "Se7en","1995",
    "In search of a murderer who follows the seven deadly sins.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
        "https://www.youtube.com/watch?v=J4YV2_TcCoE")
gladiator = movies.Movie(
    "Gladiator","2000",
    "A gladiator gets revenge and saves Rome.",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=AxQajgTyLcM")
american_beauty = movies.Movie(
    "American Beauty","1999",
    "A man finds peace.",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
    "https://www.youtube.com/watch?v=hIq9Zjw0mm8")
charade = movies.Movie(
    "Charade","1963",
    "A woman is caught in the wake of her husband's murder.",
    "https://upload.wikimedia.org/wikipedia/en/e/ec/Charade_movieposter.jpg",
    "https://www.youtube.com/watch?v=NMkeqjacvAU")
amelie = movies.Movie(
    "Amelie","2001","An unusual girl lives her life.",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
    "https://www.youtube.com/watch?v=sECzJY07oK4")
snatch = movies.Movie(
    "Snatch","2000",
    "A diamond theft and intertwining storylines meet.",
    "https://ok2disconnectportfolio.files.wordpress.com/2011/05/snatch-poster1.jpg",
    "https://www.youtube.com/watch?v=Q8jbt0wBkMI")
holy_grail = movies.Movie(
    "Monty Python and the Holy Grail","1975",
    "King Arthur and his knights seek the grail.",
    "http://www.themoviegeek.com/movie_graphics/1177.jpg",
    "https://www.youtube.com/watch?v=RDM75-oXGmQ")
good_will_hunting = movies.Movie(
    "Good Will Hunting","1997",
    "Will Hunting's genius is recognized, but he still has a lot to learn.",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=QSMvyuEeIyw")
fountain = movies.Movie(
    "The Fountain", "2006",
    "The love of a couple rises anew like water in a fountain.",
    "https://upload.wikimedia.org/wikipedia/en/e/ee/Fountain_poster_1.jpg",
    "https://www.youtube.com/watch?v=dAuxryJ6pv8")
v_for_vendetta = movies.Movie(
    "V for Vendetta","2005",
    "Dystopian society is saved by a masked man.",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
    "https://www.youtube.com/watch?v=k_13fFIrhPk")

movies = [pi, shawshank_redemption,good_will_hunting,fountain,v_for_vendetta,thank_you_for_smoking,garden_state,
        fifth_element,dark_knight,se7en,gladiator,american_beauty,charade,amelie,snatch,holy_grail]
fresh_tomatoes.open_movies_page(movies)
