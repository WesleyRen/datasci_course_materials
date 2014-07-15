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
    # initiate two dicts, one for none_sent, one for sentiment words
    none_sent_scores = {}
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
            line_score = 0.0
            # score the line:
            for w in words:
                if w in scores:
                    line_score = line_score + scores[w]
            if line_score != 0:
                for w in words:
                    if w not in scores:
                        if w not in none_sent_scores:
                            none_sent_scores[w] = line_score
                        else:
                            none_sent_scores[w] = none_sent_scores[w] + line_score
    
    for w in none_sent_scores:
        print w.encode('utf8'), none_sent_scores[w]


if __name__ == '__main__':
    main()
