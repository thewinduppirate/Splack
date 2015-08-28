#!/usr/bin/env python3
# Based on a quick script on the ArchLinux wiki
# Not sure playerctl is the best way to go

import urllib.request
import urllib.parse
import json

webhookURL =  #CHANGE

def send():
    params = {
    "text" : "This is posted to <#general> and comes from *Bot*.",
    "channel" : "@tom",
    "username" : "Bot",
    "icon_emoji" :":headphones:",
    }

    postparams = urllib.parse.urlencode(params)

    # payload = urllib.parse.urlencode(params)
    # payload = payload.encode("utf-8")
    
    data = json.dumps(params)

    payload = data.encode("utf-8")

    request = urllib.request.Request(webhookURL, payload, {'Content-Type': 'application/json'})

    f = urllib.request.urlopen(request)
    response = f.read()
    f.close()


if __name__ == "__main__":
    try:
        send()
    except KeyboardInterrupt:
        print("\nApplication Terminated...\n")