from app import app
import urllib.request,json
from ..models import Source,Article



api_key = None
base_url = None
article_url = None


def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_URL']

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

def get_articles(id): #searches the articles by id of a particular source
    url_format = article_url.format(id,api_key)
    
    with urllib.request.urlopen(url_format) as url:
         url_response  = url.read()
         response_format = json.loads(url_response)

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
       image  = item.get('urlToImage')
       url = item.get('url')
       timeOfPublish = item.get('publishedAt')
       
       
       new_article = Article(id,author,title,description,image , url, timeOfPublish)
       articles_list.append(new_article)


    return articles_list



    