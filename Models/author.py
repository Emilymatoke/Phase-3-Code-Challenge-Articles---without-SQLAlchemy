

class Author:
    def __init__(self, name):
        # check if the name is valid
        """ Name must be a string longer than 0 characters in length"""
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError(" Name must be a string and not empty")
        self._name = name
        self._articles = []

    #getter for name
    @property
    def name(self):
        """The name property"""
        return self._name

    
        

    '''def __setattr__(self, name, value):
        if name != "name" and hasattr(self, name):
            raise AttributeError("Attribute '{}' cannot be modified".format(name))
        super().__setattr__(name, value)'''

    def articles(self):
        return self._articles

    #creating a new article instance
    def add_article(self, magazine, title):
        from articles import Article
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    #return a unique list of strings
    def topic_areas(self):
        categories = set()
        for article in self._articles:
            categories.add(article.magazine.category)
        return list(categories) if categories else None
    
    #return a unique list of magazine which an author has contributed to
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
from articles import Article

from magazine import Magazine