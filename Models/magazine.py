
class Magazine:

    _all_magazines = set()

    def __init__(self, name, category):
        #check if name and category meet the requirements
        if not isinstance(name, str) or not isinstance(category,str) or len(name) < 2 or len(name) >16 or len(category) == 0:
             raise ValueError("Name must be a str between 2 and 16 characters and category should not be empty")

       
        self._name = name
        self._category = category
        self._articles = [] #store my articles
        self._contributors = set()
        Magazine._all_magazines.add(self)

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        """Name must be a string between 2 and 16 characters in length"""
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must have at least one character")
    #return all articles
    def articles(self) :
        return self._articles
    
    #add an article to magazine
    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        #self._contributors.add(author)
        return article
    
    #return list of articles
    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    #return contributors
    def contributors(self) :
        #collect unique authors
        return list(set(article.author for article in self._article if isinstance(article.author, Author)))
    
    
    #return a list of authors with more than two articles
    def contributing_authors(self):
        #collect unique authors
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author in authors_count:
                authors_count[author] += 1
            else:
                authors_count[author] = 1

        #filter authors with more than 2 articles
        return [author for author, count in authors_count.items() if count > 2] if authors_count else None
    
    #return article_title


    @classmethod
    def top_publisher(cls):
        all_magazines = cls._all_magazines
        if all_magazines:
            return max(all_magazines, key=lambda magazine: len(magazine.articles()))
        return None

     
from articles import Article
from author import Author
