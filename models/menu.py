from models.database import Database


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
        blog = Database.find_one('blogs', {'author': self.user}) is not None
        if blog is not None:
            self.user_blog = blog
            return True
        else:
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
            # allow user to pick one
            # display posts
            pass
        # if write
        elif read_or_write == 'W':
            # check if user has a blog
            # if they do, prompt to write a post
            # if not, prompt to create new blog
            pass
        else:
            print('Thank you for blogging!')
            
