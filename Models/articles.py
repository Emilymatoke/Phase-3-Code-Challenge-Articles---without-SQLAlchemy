
class Article:
    def __init__(self, author, magazine, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be between 5 and 50 characters.")
        
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")

        self.author = author
        self.magazine = magazine
        self._title = None  # Initialize _title to None

        # Title will be set using the setter method below

    @property
    def title(self):
        """The title property"""
        return self._title

   
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        self._magazine = value

# Import the Author class from author.py
from author import Author

# Import the Magazine class from magazine.py
from magazine import Magazine
