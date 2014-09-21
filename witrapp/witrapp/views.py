from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

import urllib2


@view_config(route_name='home', renderer='templates/index.mako')
def home(request):
    response = urllib2.urlopen('http://witr.rit.edu/static/live.m3u')
    response = response.read()
    print response
    return {'response': response}

@view_config(route_name='all_songs_play', renderer='witrapp:templates/allsongs.mako')
def all_songs_play(request):
    pass

