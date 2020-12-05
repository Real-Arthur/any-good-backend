import json
import requests
import os
from flask import Flask, jsonify, request
from decouple import config

def searchPerson(value):   
    API_KEY = config('API_KEY')
    url = 'https://api.themoviedb.org/3/search/person'
    params = dict(
        api_key=API_KEY,
        query=value,
        page=1
    )
    resp = requests.get(url=url, params=params)
    data = resp.json()
    print(data['results'])
    return data
