class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 2 and 16 characters in length"""
        if isinstance(name, str) and 2 < len(name) > 16 :
            self._name = name
        else :
            raise ValueError("Name must be between 2 and 16 characters")
        

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else :
            raise ValueError("Category must have at least one character")
        
    def articles(self):
        return [article for article in self._articles if isinstance(article, Article)]

    def contributors(self):
        return list({article.author for article in self._articles if isinstance(article, Article)})

