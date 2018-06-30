# models is container with class Post
# basis for object oriented programming
from models.post import Post

# an instance of class
post = Post('Hello', 'World', 'Matt')
# post.content = 'changed content'

print(post.content)