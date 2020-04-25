# cbcplayer
python cli cbc radio player
---------------------------

A curses program for streaming CBC Radio One

Requires MPD and MPC

## Files:

### cbc_playlist.m3u.json

A JSON file containing all Canadian Broadcasting Corporation (CBC) online Radio streaming URL's. This may not be a complete list but covers the main URL's available in Canada, available through the 'Live Radio' link at cbc.ca

Format: id: unique identifier
        stat: can be used in any way; I use it designate my preferred station with a 1
        title: name of station
        url: URL of audio stream

### player.ini

For configuration settings

### cbcplayer.bak.py

Python3 script
