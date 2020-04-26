from app import app
import urllib.request,json
from .models import source,article

Source = source.Source
Article = article.Article

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']
article_url = 'http://newsapi.org/v2/everything?sources={}&apiKey={}'

def get_sources(category):
    url_format = base_url.format(category,api_key)

    with urllib.request.urlopen(url_format) as url:
        url_response = url.read()
        new_url_response = json.loads(url_response)

        sources_list_of_obj = None

        if new_url_response['sources']:
            sources_list_of_dicts   =  new_url_response['sources']  #returns a list of dictionaries 
            sources_list_of_obj = process(sources_list_of_dicts)  #returns a list of objects after calling the process() function on the sources_list_of_dicts

    return sources_list_of_obj


def process(list_of_dicts):   # function that processes a list of dictionaries converting each into an object and appending each into a list

    sources_list = []

    for item in list_of_dicts:
       id    = item.get('id')
       name  = item.get('name')
       description  = item.get('description')
       url   = item.get('url')

       new_source = Source(id,name,description,url)
       sources_list.append(new_source)

    return sources_list

def get_articles(source_name): #searches the articles by name of a particular source
    url_format = article_url.format(source_name,api_key)
    
    with urllib.request.urlopen(url_format) as url:
         url_response  = url.read()
         response_format = json.load(url_response)

         articles_list_of_obj = None

         if response_format['articles']:
             articles_list_of_dict = response_format['articles']
             articles_list_of_obj = process_results(articles_list_of_dict)

    return articles_list_of_obj


def process_results(list_of_dicts):   # function that processes a list of dictionaries converting each into an object and appending each into a list

    articles_list = []

    for item in list_of_dicts:
       id    = item.get('id')
       author  = item.get('author')
       description  = item.get('description')
       title   = item.get('title')
       image   = item.get('urlToImage')

       if image:
           new_article = Article(id,author,title,description,image)
           articles_list.append(new_source)
           

       
       

    return articles_list



    