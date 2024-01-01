from flask import Flask, render_template
import os
from flask_frozen import Freezer
root_path = os.getcwd()
app = Flask(__name__)

freezer = Freezer(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    freezer.run(debug=True)