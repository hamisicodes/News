from app import app
from flask import render_template
from .requests import get_sources,get_articles

@app.route('/')
def index():
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    science_sources = get_sources('science')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    return render_template('index.html' , sports_sources = sports_sources , general_sources = general_sources , science_sources = science_sources , business_sources = business_sources, technology_sources = technology_sources)


@app.route('/source/<id>')
def sources(id):
    articles = get_articles(id)
    return render_template('articles.html' , name = id , articles = articles)