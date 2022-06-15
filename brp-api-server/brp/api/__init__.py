import os
import pathlib
import yaml

from flask import Flask, Response
from pymongo import MongoClient

app = Flask(__name__)

mongo_client: MongoClient = MongoClient('mongo', 27017, username='root', password='password')

@app.route('/')
def hello_world():
    return 'hello,world!'


@app.route('/init')
def init():
    db = mongo_client['brp']

    for yml_file in pathlib.Path('/database').glob('*.yml'):
        collection_name = os.path.splitext(os.path.basename(yml_file))[0]

        collection = db[collection_name]
        with open(yml_file, 'rb') as yml_file_stream:
            for yaml_data in yaml.load_all(yml_file_stream, Loader=yaml.SafeLoader):
                collection.insert_one(yaml_data)

    return Response(status=200)