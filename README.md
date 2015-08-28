Splack
======

##Spotify notifications on Slack.

##Aim
The aim is to somehow get spotify notifications from the office music laptop to the #General slack channel. 

* Stage 1 - Passive, as they happen. 
* Stage 2 - Use slash command to query. (Going to be far more complicated.)

##Stage 1
Is done. Splack.py is a python script that listens for the notifications, and 
then uses a WebHook to push that info to the chosen channel. Just change defaults and run in the 
background. 

##Reqs
* playerctl
* GLib
* urllib
* json
