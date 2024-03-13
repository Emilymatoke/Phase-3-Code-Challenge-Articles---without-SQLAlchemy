from author import Author
from magazine import Magazine
from articles import Article

# Create authors
author1 = Author("Sam Smith")
author2 = Author("Wendy Williams")

# Create magazines
magazine1 = Magazine("Tech Magazine", "Technology")
magazine2 = Magazine("Fashion Weekly", "Fashion")

# Add articles
article1 = author1.add_article(magazine1, "10 Tips for Better Coding")
article2 = author1.add_article(magazine2, " Winter Fashion Trends for 2024")
article3 = author2.add_article(magazine2, "How to Dress for Work")

# Print article details
print("Article 1:")
print("Author:", article1.author.name)
print("Magazine:", article1.magazine.name)
print("Title:", article1.title)
print()

print("Article 2:")
print("Author:", article2.author.name)
print("Magazine:", article2.magazine.name)
print("Title:", article2.title)
print()

print("Article 3:")
print("Author:", article3.author.name)
print("Magazine:", article3.magazine.name)
print("Title:", article3.title)
print()

# Display top publisher
top_publisher = Magazine.top_publisher()
if top_publisher:
    print("Top Publisher:", top_publisher.name)
else:
    print("There are no magazines.")
                               

