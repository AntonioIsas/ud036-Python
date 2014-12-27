import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy an his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                        "Using rock music to learn",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

hunger_games = media.Movie("Hunger Games",
                     "A eally real reality show",
                     "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, hunger_games]
fresh_tomatoes.open_movies_page(movies)
