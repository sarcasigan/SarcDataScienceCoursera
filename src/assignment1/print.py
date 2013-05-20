import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
jsontemp = json.load(response)

length = len(jsontemp["results"])

for i in range(0, 10):
    print jsontemp["results"][i]["text"].encode('ascii', 'ignore')
    