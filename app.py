# models is container with class Post
# basis for object oriented programming
from models.post import Post
from models.database import Database

# initialize db
Database.initialize()

# an instance of class
# post = Post(blog_id='123',
#             title='Singularity',
#             content='Is near',
#             author='Bob')
# post.save_to_mongo()

# find_id = Post.from_mongo('33501ef603e24ded9ea94549581438b7')
# print('find', find_id)

# posts = Post.from_blog('123')
# # print(posts)
# for post in posts:
#     print(post)

# blog class
blog = Blog(author='Matt',
            title='Sample title',
            description='sample description')

blog.new_post()