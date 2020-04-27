class Source:
    def __init__(self , id , name , description , url):
        
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Article:
    def __init__(self,id,author,title,description,image,url,timeOfPublish):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.image = image
        self.url = url
        self.timeOfPublish = timeOfPublish
        