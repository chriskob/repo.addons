from os.path import splitext
from re      import findall
from urllib2 import unquote, urlopen
from random  import random, shuffle

import xbmc, xbmcgui


results  = []
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
# change to your actual server
my_url   = "http://chrisk.ddns.net:81/kodi/cartoons/The_Flintstones/"
# regular expression to parse file data from your page
regex    = '<tr><td.*?src="(.*?)".*?[VID].*?href="(.*?)">'# .*?ht">(.*?)  </.*?ht">(.*?)</td'

# open connection to your server
cached   = urlopen(my_url)
# read source
source   = cached.read()
# close connection
cached.close()
# clear the playlist... (probably not needed)
playlist.clear()

# iterate through list of found regex results
results = findall(regex, source)
shuffle(results, random)
for index, vid in enumerate(results):
    # clean the text from the filename (unquote), remove file extension (splitext), set as title
    listitem = xbmcgui.ListItem(splitext(unquote(vid[1]))[0], thumbnailImage=my_url + vid[0])
    # add items to playlist
    playlist.add(my_url + vid[1], listitem, index=index)

# start playing
xbmc.Player().play(playlist)