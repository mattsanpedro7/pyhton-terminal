# things that have same properties
class Post(object):

    # which properties the post should have
    # init: method I am going to create...
    def __init__(self, title, content, author):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id

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