from flask import render_template, url_for, flash, redirect, request
from ZhaoSite import app

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/music')
def music():
    return render_template('music.html', title='Music')

@app.route('/basketballstats')
def basketballstats():
    return render_template('stats.html', title='Basketball Stats')

