# twitter_diff

## Description
This script will tell you the users specific to each one of your lists on Twitter : followers & following.

## Requirements
* Python 2.6+
* Twitter module for Python (pip install twitter)

## Execution
First, create a conf.json file with you application keys and the tokens of the account you want to treat.
Then, just launch the script diff.py, it will return something like that :
```
5623 friends (users subscribed by the account).
8422 followers (users following the account).


256 friendsOnly : [ <ids list> ]

528 followersOnly : [ <ids list> ]
```