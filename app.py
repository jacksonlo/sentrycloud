from flask import Flask, render_template, request
from data import get_data, count, create_word_cloud
import os.path

app = Flask(__name__)


@app.route("/")
def index():
    field = request.args.get('field', 'title')
    if not os.path.isfile(field):
        data = get_data()
        counts = count(data, field)
        create_word_cloud(counts, 'static/{}.png'.format(field))

    return render_template('index.html', context={'field': field})
