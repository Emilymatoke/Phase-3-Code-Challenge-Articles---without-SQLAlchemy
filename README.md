# Phase-3-Code-Challenge-Articles---without-SQLAlchemy
Core Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.
Initializers and Properties
Author

    Author __init__(self, name)
        Author is initialized with a name
    Author property name
        Returns the author's name
        Names must be of type str
        Names must be longer than 0 characters
        Should not be able to change after the author is instantiated.
        hint: hasattr()

Magazine

    Magazine __init__(self, name, category)
        A magazine is initialized with a name and a category
    Magazine property name
        Returns the magazine's name
        Names must be of type str
        Names must be between 2 and 16 characters, inclusive
        Should be able to change after the magazine is instantiated.
    Magazine property category
        Returns the magazine's category
        Categories must be of type str
        Categories must be longer than 0 characters
        Should be able to change after the magazine is instantiated.

Article

    Article __init__(self, author, magazine, title)
        Article is initialized with an Author instance, a Magazine instance, and a title.
    Article property title
        Returns the article's title
        Titles must be of type str
        Titles must be between 5 and 50 characters, inclusive
        Should not be able to change after the article is instantiated.
        hint: hasattr()

Object Relationship Methods and Properties
Article

    Article property author
        Returns the author object for that article
        Must be of type Author
        Authors can be changed after the article object is initialized
    Article property magazine
        Returns the magazine object for that article
        Must be of type Magazine
        Magazines can be changed after the article object is initialized

Author

    Author articles()
        Returns a list of all the articles the author has written
        Must be of type Article
    Author magazines()
        Returns a unique list of magazines for which the author has contributed to
        Must be of type Magazine

Magazine

    Magazine articles()
        Returns a list of all the articles the magazine has published
        Must be of type Article
    Magazine contributors()
        Returns a unique list of authors who have written for this magazine
        Must be of type Author

Aggregate and Association Methods
Author

    Author add_article(magazine, title)
        Receives a Magazine instance, and a title as arguments
        Creates and returns a new Article instance and associates it with that author, the magazine provided
    Author topic_areas()
        Returns a unique list of strings with the categories of the magazines the author has contributed to
        Returns None if the author has no articles

Magazine

    Magazine article_titles()
        Returns a list of the titles strings of all articles written for that magazine
        Returns None if the magazine has no articles
    Magazine contributing_authors()
        Returns a list of authors who have written more than 2 articles for the magazine
        Authors must be of type Author
        Returns None if the magazine has no authors with more than 2 publications

Advanced Deliverables

These deliverables are not required to pass the code challenge, but if you have the extra time, or even after the code challenge, they are a great way to stretch your skills.
Bonus: Aggregate and Association Method

    Magazine classmethod top_publisher()
        Returns the Magazine instance with the most articles
        Returns None if there are no articles.
        Uncomment lines 206-224 in the magazine_test file
        hint: will need a way to remember all magazine objects

Bonus: For any invalid inputs raise an Exception

    First, comment out the following lines
        article_test.py
            lines 28-29
        author_test.py
            lines 31-32, and 35-36
        magazine_test.py
            lines 31-32, 47-48, 51-52, 84-85, and 100-102
    Then, uncomment the following lines in the test files
        article_test.py
            lines 34-35, 46-47, and 50-51
        author_test.py
            lines 39-40, and 53-54
        magazine_test.py
            lines 35-36, 55-56, 59-60, 90-91, and 105-106
