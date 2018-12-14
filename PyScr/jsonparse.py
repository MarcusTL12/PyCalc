import os

def parse(filename):
	with open(filename, "r") as i, open("tempjson.py", "w") as o:
		o.write("a = ")
		for l in i:
			o.write(l.replace("true", "True").replace("false", "False").replace("null", "None"))
	import tempjson
	os.remove("tempjson.py")
	return tempjson.a

