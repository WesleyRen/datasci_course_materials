import sys, json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)
    line_sentiment_score(sent_file, tweet_file)
def line_sentiment_score(sent_dict_file, target_file):
    scores = {};
    for s in sent_dict_file:
        term, score = s.split('\t')
        scores[term] = int(score)
    for t in target_file:
        tweet = json.loads(t)
        # only process if the line is a tweet.
        if "text" in tweet:
            # print tweet
            words = tweet["text"].split()
            line_score = 0
            # score the line:
            for w in words:
                if w in scores:
                    line_score = line_score + scores[w]
            print line_score
    

if __name__ == '__main__':
    main()
