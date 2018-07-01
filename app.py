# models is container with class Post
# basis for object oriented programming
from models.post import Post
from models.database import Database

# initialize db
Database.initialize()

# an instance of class
post = Post('Hello', 'World', 'Matt')
# post.content = 'changed content'

print(post.content)