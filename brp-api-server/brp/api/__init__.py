import os
import pathlib
import yaml

from flask import Flask, Response, render_template
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

mongo_client: MongoClient = MongoClient('mongo', 27017, username='root', password='password')


@app.route('/')
def hello_world():
    return render_template('table.html')


@app.route('/init')
def init():
    mongo_database = mongo_client['brp']

    for yml_file in pathlib.Path('/database').glob('*.yml'):
        collection_name = os.path.splitext(os.path.basename(yml_file))[0]

        mongo_collection = mongo_database[collection_name]
        with open(yml_file, 'rb') as yml_file_stream:
            for yaml_data in yaml.load_all(yml_file_stream, Loader=yaml.SafeLoader):
                mongo_collection.insert_one(yaml_data)

    return Response(status=200)


@app.route('/column/<collection_name>')
def column(collection_name):
    mongo_database = mongo_client['brp']
    mongo_collection = mongo_database['column']
    result = mongo_collection.find_one({ 'collection': collection_name })

    return Response(
        json_util.dumps(result),
        mimetype='application/json'
    )


@app.route('/machine/')
def machine():
    mongo_database = mongo_client['brp']
    mongo_collection = mongo_database['machine']
    result = mongo_collection.find()

    return Response(
        json_util.dumps(result),
        mimetype='application/json'
    )