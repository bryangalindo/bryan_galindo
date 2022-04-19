from flask import render_template, Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/resume')
def resume():
    return redirect('https://drive.google.com/file/d/1gajvDpSws0ZsaSDuit01FUL3I4Rzj3gK/view?usp=sharing')
