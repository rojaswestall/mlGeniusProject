# https://docs.genius.com/

import requests
import urllib2
import json

AUTH_TOKEN = "4OJhKq4UxyXPDNw9BM9BxvLwHtdGxcmwTtPzv_toigTps1vaVvbYow8cg-v0A5z4"

# Search genius, given a string. Search can return anything
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

# Return the id of an artist given a search term
def genius_search_artist(artist):
    songres = genius_search(artist)
    hits = songres['response']['hits']

    if len(songres['response']['hits']) == 0:
        print 'There were no artists that matched the search'
        return -1
    else:
        return songres['response']['hits'][0]['result']['primary_artist']['id']

# Get songs for an artist given an artists ID
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
    res = genius_search_artist('Post Malone')
    print json.dumps(res, indent=4)
    # # print res
    # print '\n'
    # print res.viewkeys()
    # print "\n"
    # print [key for key in res['response']['hits'][0]['result']]

    # res = genius_artist_songs('16775')
    # for i in range(len(res['response']['songs'])):
    #     print res['response']['songs'][i]['full_title']
