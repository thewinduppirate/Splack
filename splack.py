#!/usr/bin/env python3
# Based on a quick script on the ArchLinux wiki
# Not sure playerctl is the best way to go

from gi.repository import Playerctl, GLib
import urllib.request
import urllib.parse
import json

SlackWebhookURL = #CHANGE
SlackBotName = "Bot"
SlackChannel = "@tom"

player = Playerctl.Player()

# On track change print out track info (for the moment)
def on_track_change(player, e):
    track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
    splackinfo={"text": [track_info], "channel": "#general", "username": "SplackBot", "icon_emoji": ":headphones:"}
    print([track_info])
    send([track_info])

def send(track_info):
	params = {
    "text" : track_info,
    "channel" : SlackChannel,
    "username" : SlackBotName,
    "icon_emoji" :":headphones:",
    }

    postparams = urllib.parse.urlencode(params)

    data = json.dumps(params)

    payload = data.encode("utf-8")

    request = urllib.request.Request(SlackWebhookURL, payload, {'Content-Type': 'application/json'})

    f = urllib.request.urlopen(request)
    response = f.read()
    f.close()

player.on('metadata', on_track_change)

GLib.MainLoop().run()