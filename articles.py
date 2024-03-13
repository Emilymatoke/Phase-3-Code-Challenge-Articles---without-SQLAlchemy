class Article :
    def __init__(self, author, magazine, title) :
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string ranging 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title (self) :
        """The title property"""
        return self._title
    
    
    