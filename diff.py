#!/usr/bin/python3
from twitter import *
import time
import json
with open('./conf.json') as file: conf = json.load(file)

tw = Twitter(auth=OAuth(conf['token'], conf['token_key'], conf['con_sec'], conf['con_sec_key']))
maxcount = 5000
friends = []
followers = []

res = tw.friends.ids(count=maxcount)
cursor = -1
while cursor != 0:
    for id in res['ids']: friends.append(id)
    cursor = res['next_cursor']
    res = tw.friends.ids(count=maxcount,cursor=res['next_cursor'])

res = tw.followers.ids(count=maxcount)
cursor = -1
while cursor != 0:
    for id in res['ids']: followers.append(id)
    cursor = res['next_cursor']
    res = tw.followers.ids(count=maxcount,cursor=cursor)

print("%s friends (users subscribed by the account)." % len(friends))
print("%s followers (users following the account)." % len(followers))
print("\n")

friendsOnly = list(set(friends) - set(followers))
followersOnly = list(set(followers) - set(friends))
print("%i friendsOnly : %s\n" % (len(friendsOnly), friendsOnly))
print("%i followersOnly : %s\n" % (len(followersOnly), followersOnly))
