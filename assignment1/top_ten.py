import sys, json

def hw():
    print 'Hello, world!'

def main():
    tweet_file = open(sys.argv[1])
    top_ten(tweet_file)
def top_ten(tweet_file):
    freq = {};
    total = 0.0;
    for t in tweet_file:
        tweet = json.loads(t)
        # only process if the line is a tweet.
        if "entities" in tweet:
            hashtags = tweet["entities"]["hashtags"]
            for h in hashtags:
                if "text" in h:
                    total += 1
                    if h["text"] not in freq:
                        freq[h["text"]] = 1
                    else:
                        freq[h["text"]] += 1
    # print total
    # for w in freq:
    #     print w.encode('utf8'), float(freq[w]/total)
    i = 0
    for w in sorted(freq, key=freq.get, reverse=True):
        i += 1
        print w.encode('utf8'), freq[w]
        if i == 10:
            return  

if __name__ == '__main__':
    main()
