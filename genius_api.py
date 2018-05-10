# https://docs.genius.com/

import requests
import urllib2
import json

AUTH_TOKEN = ""


def genius_search(term):
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


def genius_artist_songs(artist_id):
    _URL_API = "https://api.genius.com/"
    _URL_ARTIST = "artists/{}/songs?sort=popularity&per_page=50".format(artist_id)
    querystring = _URL_API + _URL_ARTIST
    request = urllib2.Request(querystring)
    request.add_header("Authorization", "Bearer " + AUTH_TOKEN)
    request.add_header("User-Agent", "")

    response = urllib2.urlopen(request, timeout=3)
    raw = response.read()
    json_obj = json.loads(raw)
    return json_obj


if __name__ == '__main__':
    # res = genius_search('Andy Shauf')
    # print res.viewkeys()
    # print "\n"
    # print [key for key in res['response']['hits'][0]['result']]

    # res = genius_artist_songs('16775')
    # for i in range(len(res['response']['songs'])):
    #     print res['response']['songs'][i]['full_title']
