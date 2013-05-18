import sys
import json

scores = {} # the sentiment scores
statescore = {}
 
def get_sentiment_per_line(line):
    partialscore = 0
    words = line.split()
    for word in words:
        if word in scores:            
            partialscore += scores[word]
    return partialscore
            
def parseTweetFile(tweetFile):
    partial_score = 0    
    for line in tweetFile:
        tweetjson = json.loads(line)
        if tweetjson.has_key("place"):
            if tweetjson["place"] == None:
                continue
            else:
                country = tweetjson["place"]["country_code"].encode('ascii', 'ignore')
                if country == "US":
                    if tweetjson.has_key("text"):
                        tweet = tweetjson["text"].encode('ascii', 'ignore')
                        partial_score = get_sentiment_per_line(tweet)
                    place = tweetjson["place"]["full_name"].encode('ascii', 'ignore')
                    state = place.split(",")
                    state[0] = state[0].strip()
                    state[1] = state[1].strip()
                    if state[1] in statescore:
                        statescore[state[1]] += partial_score
                    else:
                        statescore[state[1]] = partial_score
                            
def main():
    sent_file = open(sys.argv[1], "r")
    tweet_file = open(sys.argv[2], "r")    
    
    # convert from file to dictionary format
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    parseTweetFile(tweet_file)        
    
    print max(statescore.iterkeys(), key=(lambda key: statescore[key]))
    
    sent_file.close()
    tweet_file.close()
    
if __name__ == '__main__':
    main()
