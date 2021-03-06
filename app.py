from flask import render_template, Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/resume')
def resume():
    return redirect('https://drive.google.com/file/d/1xBXerPn02dEXV7t-D-REJZaQbF6kYC_v/view?usp=sharing')


@app.route('/breakoutlevels')
def breakouts():
    return redirect('https://archive.ph/YNd5H')


@app.route('/ebayscraper')
def ebayscraper():
    return redirect('https://github.com/bryangalindo/scrape/blob/master/ebayscrape.py')


@app.route('/rankmebby')
def rankmebby():
    return redirect('https://rankmebby.com/collections/metabaes?id=622')


@app.route('/tamalemkt')
def tamalemkt():
    return redirect('https://tamalemkt.com')
