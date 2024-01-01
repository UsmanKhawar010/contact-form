from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__, static_folder='static', static_url_path='/static')
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    freezer.freeze()
