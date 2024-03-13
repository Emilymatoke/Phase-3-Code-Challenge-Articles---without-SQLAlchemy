# Import the Author class from author.py
from author import Author

# Import the Magazine class from magazine.py
from magazine import Magazine

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None  # Initialize _title to None

        # Title will be set using the setter method below

    @property
    def title(self):
        """The title property"""
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            raise ValueError("Title must be between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        self._magazine = new_magazine
