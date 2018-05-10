# https://docs.genius.com/

import requests
import urllib2
import json

AUTH_TOKEN = "4OJhKq4UxyXPDNw9BM9BxvLwHtdGxcmwTtPzv_toigTps1vaVvbYow8cg-v0A5z4"


def genius_search(term):
    """Search genius, given a string. Search can return anything"""
    _URL_API = "https://api.genius.com/"
    _URL_SEARCH = "search?q="
    querystring = _URL_API + _URL_SEARCH + urllib2.quote(term)
    request = urllib2.Request(querystring)
    request.add_header("Authorization", "Bearer " + AUTH_TOKEN)
    request.add_header("User-Agent", "")

    response = urllib2.urlopen(request, timeout=3)
    raw = response.read()
    json_obj = json.loads(raw)
    return json_obj


def genius_search_artist(artist):
    """Return the id of an artist given a search term"""
    songres = genius_search(artist)
    # hits = songres['response']['hits']
    if len(songres['response']['hits']) == 0:
        print 'There were no artists that matched the search'
        return -1
    else:
        return songres['response']['hits'][0]['result']['primary_artist']['id']


def genius_artist_songs(artist_id, num):
    """ Get songs for an artist given an artists ID"""
    _URL_API = "https://api.genius.com/"
    _URL_ARTIST = "artists/{}/songs?sort=popularity&per_page={}".format(artist_id, str(num))
    querystring = _URL_API + _URL_ARTIST
    request = urllib2.Request(querystring)
    request.add_header("Authorization", "Bearer " + AUTH_TOKEN)
    request.add_header("User-Agent", "")

    response = urllib2.urlopen(request, timeout=3)
    raw = response.read()
    json_obj = json.loads(raw)
    return json_obj


if __name__ == '__main__':

    artists = ["2Pac", "Eminem", "Ice Cube", "Outkast", "Nas", "DMX", 
               "The Game", "T.I.", "Kanye West", "Kendrick Lamar"]
    for at in artists:
        at_id = genius_search_artist(at)

        if at_id == -1:
            continue
        print "\n"
        print at
        at_songs = genius_artist_songs(at_id, 5)
        for i in range(len(at_songs['response']['songs'])):
            print at_songs['response']['songs'][i]['full_title']
