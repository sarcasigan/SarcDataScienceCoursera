import sys
import json
from collections import OrderedDict

hashtags = {}
           
def parseTweetFile(tweetFile):    
    for line in tweetFile:
        tweetjson = json.loads(line)
        if tweetjson.has_key("entities"):
            entity = tweetjson["entities"]
            if entity.has_key("hashtags"):
                hashtaglist = entity["hashtags"]
                for unit in hashtaglist:
                    if unit.has_key("text"):
                        hashtag = unit["text"].encode("ascii", "ignore").strip()
                        if hashtag == None:
                            continue
                        elif hashtags.has_key(hashtag):
                            hashtags[hashtag] += 1.0
                        else:
                            hashtags[hashtag] = 1.0                        
                            
def main():
    tweet_file = open(sys.argv[1], "r")    
        
    parseTweetFile(tweet_file)        
    
    toptensorted = OrderedDict(reversed(sorted(hashtags.items(), key=lambda x: x[1])))
    
    for i in range(10):
        print toptensorted.keys()[i], toptensorted[toptensorted.keys()[i]]
        
    tweet_file.close()
    
if __name__ == '__main__':
    main()
