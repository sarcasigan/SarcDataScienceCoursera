import sys
import json

scores = {} # the sentiment scores
newScores = {}
 
def get_sentiment_per_line(line):
    partialscore = 0
    words = line.split()
    for word in words:
        if word in scores:            
            partialscore += scores[word]
    print partialscore
            
def parseTweetFile(tweetFile):    
    for line in tweetFile:
        tweetjson = json.loads(line)
        if tweetjson.has_key("text"):
            tweet = tweetjson["text"].encode('ascii', 'ignore')
            get_sentiment_per_line(tweet)
        else:
            print 0

def main():
    sent_file = open(sys.argv[1], "r")
    tweet_file = open(sys.argv[2], "r")    
    
    # convert from file to dictionary format
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        newScores[term] = 0    
    
    parseTweetFile(tweet_file)        
    
    sent_file.close()
    tweet_file.close()
    
if __name__ == '__main__':
    main()
