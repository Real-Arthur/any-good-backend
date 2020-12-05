import time
from search_person import searchPerson
from search_list import search_score, roundscore
# import search_list
from flask import Flask, jsonify, request

app = Flask(__name__, static_folder='./build', static_url_path='/')
@app.route('/person', methods=['GET', 'POST'])
def post_search():
    data = request.get_json()
    print(data['name'])
    results = searchPerson(data['name'])
    print(results)
    return results

@app.route('/search/<int:id>', methods=['GET', 'POST'])
def get_score(id):
    data = id
    print(data)
    results = search_score(id)
    rounded = roundscore(results)
    return str(rounded)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}
# @app.route('/search')
# def get_search_person():
#     return jsonify(search_person.name)
# @app.route('/list')
# def get_search_list():
#     # return jsonify(search_list.movies)
#     return jsonify(search_list.acting_rating)
