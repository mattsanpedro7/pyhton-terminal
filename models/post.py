# things that have same properties
import uuid
from models.database import Database


class Post(object):

    # which properties the post should have
    # init: method I am going to create...
    def __init__(self, title, content, author, date, id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        # uuid is the module
        # uuid4 method to generate => 4 is random
        # .hex 32-character hexi-decimal string
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    # what makes up this post - json representation
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    # method: post from mongo given an id and it will give us back data
    @staticmethod
    def from_mongo(id):
        # don't have to write "collection="
        # Post.from_mongo('123')
        return Database.find_one(collection='posts', query={'id', id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]


