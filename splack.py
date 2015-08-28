#!/usr/bin/env python3
# Based on a quick script on the ArchLinux wiki
# Not sure playerctl is the best way to go

from gi.repository import Playerctl, GLib
import urllib.request
import urllib.parse

webhookURL = #CHANGE

params = {}

params["text"] = "This is posted to <#general> and comes from *SplackBot*."
params["channel"] = "#general"
params["username"] = "SplackBot"
params["icon_emoji"] =":headphones:"

payload = urllib.parse.urlencode(params)
payload = data.encode("utf-8")
request = urllib.request.Request(webhookURL)
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")

player = Playerctl.Player()

# On track change print out track info (for the moment)
def on_track_change(player, e):
    track_info = '{artist} - {title}'.format(artist=player.get_artist(), title=player.get_title())
    splackinfo={"text": [track_info], "channel": "#general", "username": "SplackBot", "icon_emoji": ":headphones:"}
    print([track_info])
    with urllib.request.urlopen(request, payload) as f:
    	print(f.read())

player.on('metadata', on_track_change)

GLib.MainLoop().run()