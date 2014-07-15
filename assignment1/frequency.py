import sys, json

def hw():
    print 'Hello, world!'

def main():
    tweet_file = open(sys.argv[1])
    frequency(tweet_file)
def frequency(tweet_file):
    freq = {};
    total = 0.0;
    for t in tweet_file:
        tweet = json.loads(t)
        # only process if the line is a tweet.
        if "text" in tweet:
            # print tweet
            words = tweet["text"].split()
            for w in words:
                total += 1
                if w not in freq:
                    freq[w] = 1
                else:
                    freq[w] += 1
    # print total
    for w in freq:
        print w.encode('utf8'), float(freq[w]/total)

if __name__ == '__main__':
    main()
