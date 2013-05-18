import sys
import json

terms = {}

def count_frequency(tweet):
    words = tweet.split()
    for word in words:
        if word in terms:
            terms[word] += 1
        else:
            terms[word] = 1

def main():
    tweet_file = open(sys.argv[1], "r")
    for line in tweet_file:
        tweetjson = json.loads(line)
        if tweetjson.has_key("text"):
            tweet = tweetjson["text"].encode('ascii', 'ignore')
            count_frequency(tweet)

    frequency = 0.0
    totalterms = float(len(terms))    
    for word in terms:
        frequency = terms[word]/totalterms
        print word, str(frequency)
        
if __name__ == '__main__':
    main()
