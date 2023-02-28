# PPHA 30535
# Spring 2021
# Homework 3

# YOUR NAME HERE

# YOUR CANVAS NAME HERE
# YOUR GITHUB USER NAME HERE

# Due date: Sunday April 24th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'stars':stars}
        print(f'{title} ({year}) added to the database.')
<<<<<<< HEAD
        
    def what_to_watch(self, category=None):
        try:
            if category:
                tmp_titles = []
                for k in self.movies:
                    if self.movies[k]['category'] == category:
                        tmp_titles.append(k)
                choice = random.choice(tmp_titles)
            else:
                choice = random.choice(self.titles)
            movie = self.movies[choice]
            print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['category']}, and was given {movie['stars']} stars.")
        except ValueError:
            print('What to watch method can not be used before entering any movies.')

class InteractiveMovieDataBase(MovieDataBase):
    def __init__(self):
        super(InteractiveMovieDataBase, self).__init__()
    
    def add_movie(self, title=None, year=None, category=None, stars=None):
        if title is None:
            while 1:
                title = input('Please input the movie title: ')
                tmps = title.strip().split()
                flag = True
                for word in tmps:
                    flag = flag and word.strip().isalnum()
                if flag:
                    break
                else:
                    print('Title is required to be Strings of alphabets and numbers.')

        if year is None:
            while 1:
                try:
                    year = int(input('Please input the movie year: '))
                    break
                except Exception:
                    print('Year is required to be integer.')
        if category is None:
            while 1:
                category = input('Please input the movie category: ')
                if category.isalnum():
                    break
                else:
                    print('Category is required to be String of alphabets and numbers.')
        if stars is None:
            while 1:
                try:
                    stars = int(input('Please input the movie stars: '))
                    break
                except Exception:
                    print('Stars is required to be integer.')
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'stars':stars}
        print(f'{title} ({year}) added to the database.')
        
        def movie_rankings(self):
            movie_list = []
            for k in self.movies:
                stars = self.movies[k]['stars']
                movie_list.append((k,stars))
            movie_list.sort(key=lambda e: e[1], reverse=True)
            return [k[0] for k in movie_list]
=======

    def what_to_watch(self):
        choice = random.choice(self.titles)
        movie = self.movies[choice]
        print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['category']}, and was given {movie['stars']} stars.")
>>>>>>> parent of de39fde (Update homework 3.py)
