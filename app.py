from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/bio')
def bio():
    return render_template('bio.html')

