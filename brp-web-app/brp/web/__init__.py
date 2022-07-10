import flask

app = flask.Flask(__name__)

@app.route('/')
def root_page():
    return flask.render_template('hello-world.html')