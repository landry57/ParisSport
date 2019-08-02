from django.http import Http404
class Post():
    POSTS= [
    {'id':1 ,'Title':'First post','Body':'This is my first post'},
    {'id':2 ,'Title':'Second post','Body':'This is my second post'},
    {'id':3 ,'Title':'Third post','Body':'This is my Third post'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS


    @classmethod
    def find(cls,id):
        try:
            return cls.POSTS[int(id)-1]
        except:
            raise Http404('Sorry, post #{} not found'.format(id))
