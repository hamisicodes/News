from app import app
from flask import render_template
from .requests import get_sources

@app.route('/')
def index():
    sports_sources = get_sources('sports')
    return render_template('index.html' , sports_sources = sports_sources)