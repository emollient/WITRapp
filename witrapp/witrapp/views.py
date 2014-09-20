from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError



@view_config(route_name='home', renderer='templates/index.mako')
def home(request):
    #http://witr.rit.edu/static/live.m3u
    pass

@view_config(route_name='all_songs_play', renderer='witrapp:templates/allsongs.mako')
def all_songs_play(request):
    pass

@view_config(route_name='login_twitter')
def login_twitter(request):
    pass
