class Author :
    def __init__(self, name) :   
        self.name = name
        self._name = None
        self._articles = []

        

    @property
    def name(self) :
        """The name property"""
        return self._name 
    
    @name.setter
    def name(self, name) :
        """ Name must be a string longer than 0 characters in length"""
        if isinstance (name, str) and len(name) > 0 :
            self._name = name
        else :
            raise ValueError(" Name must be a string longer than 0 characters")
        
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("Attribute '{}' cannot be modified".format(name))
        super().__setattr__(name, value)


    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        categories = set()
        for article in self._articles:
            categories.add(article.magazine.category)
        return list(categories) if categories else None
