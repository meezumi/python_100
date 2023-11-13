# pythin class and decorators #

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged = False


# creating a decorator function:
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        # before
        if args[0].is_logged == True:
            function(args[0])
        # after

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"this is {user.name}'s new blog post")


new_user = User("aaryan")
new_user.is_logged = True
create_blog_post(new_user)
