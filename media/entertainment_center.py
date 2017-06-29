import media
import fresh_tomatoes

# Creating instances of class Movie
frozen = media.Movie("Frozen",
                     "The story of a fearless princess who sets off on a "
                     "journey alongside a rugged iceman, his loyal pet "
                     "reindeer, and a naive snowman to find her estranged "
                     "sister, whose icy powers have inadvertently trapped "
                     "the kingdom in eternal winter.",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")  # NOQA

finding_nemo = media.Movie("Finding Nemo",
                           "The story of the overprotective Ocellaris "
                           "clownfish named Marlin who, along with a regal "
                           "blue tang named Dory, searches for his abducted "
                           "son Nemo all the way to Sydney Harbour. Along the "
                           "way, Marlin learns to take risks and comes to "
                           "terms with Nemo taking care of himself.",
                           "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=3JnKU9Stmyw")  # NOQA

despicable_me = media.Movie("Despicable Me",
                            "The story of a criminal mastermind who uses a "
                            "trio of orphan girls as pawns for a grand "
                            "scheme, but then finds their love is profoundly "
                            "changing him for the better.",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=zzCZ1W_CUoI")  # NOQA

shrek = media.Movie("Shrek",
                    "The story focues on an ogre named Shrek who finds his "
                    "swamp overrun by fairy tale creatures who have been "
                    "banished there by order of the evil Lord Farquaad.",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=W37DlG1i61s")  # NOQA

cars = media.Movie("Cars",
                   "The story of a hot-shot race-car named Lightning McQueen, "
                   "who gets waylaid in Radiator Springs, where he finds the "
                   "true meaning of friendship and family.",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=WGByijP0Leo")  # NOQA

toy_story = media.Movie("Toy Story",
                        "The story focuses on the relationship between Woody, "
                        "an old-fashioned pullstring cowboy doll, and "
                        "Buzz Lightyear, an astronaut action figure, as they "
                        "evolve from rivals competing for the affections of "
                        "Andy, their owner, to friends who work together to "
                        "be reunited with Andy as his family prepares to "
                        "move to a new home.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")  # NOQA

madagascar = media.Movie("Madagascar",
                         "The story of four animals from the Central Park Zoo "
                         "who unexpectedly find themselves stranded on the "
                         "island of Madagascar.",
                         "https://upload.wikimedia.org/wikipedia/en/3/36/Madagascar_Theatrical_Poster.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=dm-eiFVtRws")  # NOQA

# Creating list of all instances of movies
movies = [frozen, finding_nemo, despicable_me, shrek, cars,
          toy_story, madagascar]

fresh_tomatoes.open_movies_page(movies)  # Opens webpage to show the movies
