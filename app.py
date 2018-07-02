# models is container with class Post
# basis for object oriented programming
from models.post import Post
from models.database import Database
from models.blog import Blog

# initialize db
Database.initialize()

###### VERIFY IF POST WORKS #######
# # an instance of class
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

# # blog class
# blog = Blog(author='Matt',
#             title='Sample title',
#             description='sample description')

# blog.new_post()

# blog.save_to_mongo()

# Blog.from_mongo()


###### VERIFY IF BLOG WORKS #######
blog = Blog(author='Matt', 
            title='Sample title',
            description='Sample description')

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())