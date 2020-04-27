from flask import render_template
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
url_for('.index'):
    general_sources = get_sources('general')
    sports_sources = get_sources('sports')
    science_sources = get_sources('science')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    entertainment_sources = get_sources('entertainment')
    return render_template('index.html' , sports_sources = sports_sources , general_sources = general_sources , science_sources = science_sources , business_sources = business_sources, technology_sources = technology_sources)


@main.route('/source/<id>')
url_for('.souces'):
    articles = get_articles(id)
    return render_template('articles.html' , name = id , articles = articles)