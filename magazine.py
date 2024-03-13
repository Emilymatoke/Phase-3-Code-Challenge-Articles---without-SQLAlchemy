class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = set()

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

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author in authors_count:
                authors_count[author] += 1
            else:
                authors_count[author] = 1
        return [author for author, count in authors_count.items() if count > 2] if authors_count else None

    def add_article(self, author, title):
        article = author.add_article(self, title)
        self._articles.append(article)
        self._contributors.add(author)
        return article

    @classmethod
    def top_publisher(cls):
        all_magazines = cls._all_magazines
        if all_magazines:
            return max(all_magazines, key=lambda magazine: len(magazine.articles()))
        return None

    _all_magazines = set()  # Assuming this line is correct
