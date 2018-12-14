import PyScr.jsonparse as json
# import json
import time

t1 = time.time()

# a = json.load(open("enemies.json", "r"))
a = json.parse("enemies.json")

t2 = time.time()

print(t2 - t1)

print(a[0]["randomshit"])