from models.database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # ask user for author name
        self.user = input('Enter your author name: ')
        self.user_blog = None
        # an underscore for a method means it's a private method
        # only the menu class should call these private methods
        # this is a convention to mean private method

        # check if they already have account
        if self._user_has_account():
            print('Welcome back {}'.format(self.user))
        else:
            # if not, prompt them to create one
            self._prompt_user_for_account()

    def _user_has_account(self):
        # adding "is not None" to end turns it to boolean
        blog = Database.find_one('blogs', {'author': self.user}) # is not None
        print('BLOG', blog)
        

        if blog is not None:
            print('TRUE SELF', self.user_blog)
            # object of type blog
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            print('FALSE SELF', self.user_blog)
            return False

    def _prompt_user_for_account(self):
        title = input('Enter blog title: ')
        description = input('Enter blog description: ')
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    # give user choice to read or write blogs
    # user create blog or account
    def run_menu(self):
        # user read or write blogs?
        read_or_write = input('Do you want to read (R) or write (W) blogs?')
        # if read:
        if read_or_write == 'R':
            # list blogs in db
            self._list_blogs()
            self._view_blog()
            # allow user to pick one
            # display posts
            # pass
        # if write
        elif read_or_write == 'W':
            # check if user has a blog
            # if they do, prompt to write a post
            self.user_blog.new_post()
            # if not, prompt to create new blog
            pass
        else:
            print('Thank you for blogging!')

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})

        for blog in blogs:
            print('ID: {}, Title: {}, Author: {}'.format(
                blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input('Enter the ID of the blog you\'d like to read: ')
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()

        for post in posts:
            print('Date: {}, Title: {}\n\n{}'.format(
                post['created_date'], post['title'], post['content']))
