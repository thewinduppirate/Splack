#!/usr/bin/env python3
# Based on a quick script on the ArchLinux wiki
# Not sure playerctl is the best way to go

from gi.repository import Playerctl, GLib
import urllib

webhookURL = #CHANGE

params {}

params["text"] = "This is posted to <#general> and comes from *SplackBot*."
params["channel"] = "#general"
params["username"] = "SplackBot"
params["icon_emoji"] =":headphones:"

payload = urllib.urlencode(params)
post = urllib.urlopen(webhookURL, params)

player = Playerctl.Player()

# On track change print out track info (for the moment)
def on_track_change(player, e):
    track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
    splackinfo={"text": [track_info], "channel": "#general", "username": "SplackBot", "icon_emoji": ":headphones:"}
    print([track_info])
    print post.read()

player.on('metadata', on_track_change)

GLib.MainLoop().run()