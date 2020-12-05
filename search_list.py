import json
import math
import requests
import os
import search_person
from decouple import config

def search_score(value):
    API_KEY = config('API_KEY')
    id = value
# calls tmdb api for full credits 
    url = f'https://api.themoviedb.org/3/person/{id}/combined_credits'
    params = dict(
        api_key=API_KEY,
        query=id
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
# full credits list 
    movies = data["cast"]
# makes empty array for vote scores
    score_list = []
# makes array of all voters scores above zero 
    for movie in movies:
        if movie["vote_average"] > 0 and movie["vote_count"] > 10:
            score_list.append(movie["vote_average"])
    print(score_list)
    print(len(score_list))      
# find average score of actor/actress
    average_score = sum(score_list)/len(score_list)
    print(average_score)
    return average_score
# rounds score to hundredth
def roundscore(average_score, decimals=2):
    multiplier = 10 ** decimals
    return math.ceil(average_score * multiplier) / multiplier