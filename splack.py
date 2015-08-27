#!/usr/bin/env python3
# Based on a quick script on the ArchLinux wiki
# Not sure playerctl is the best way to go

from gi.repository import Playerctl, GLib
import requests

webhookURL = #CHANGE

player = Playerctl.Player()

# On track change print out track info (for the moment)
def on_track_change(player, e):
    track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
	payload={"text": [track_info], "channel": "#general", "username": "SplackBot", "icon_emoji": ":headphones:"}
    print([track_info])
	requests.post(webhookURL, params=payload)

player.on('metadata', on_track_change)

GLib.MainLoop().run()
