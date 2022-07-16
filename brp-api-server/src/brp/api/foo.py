import sys
import pathlib
import flask
import json
from ruamel.yaml import YAML

yaml=YAML(typ='safe')   # default, if not specfied, is 'rt' (round-trip)

app = flask.Flask(__name__)
app.config.from_file("../../config.yml", load=yaml.load)
print(f'{app.config}')