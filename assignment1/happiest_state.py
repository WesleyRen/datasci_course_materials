import sys, json

state_to_code = {"VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU", "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI", "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID", "FEDERATED STATES OF MICRONESIA": "FM", "Armed Forces Americas": "AA", "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL", "Armed Forces Africa": "AE", "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT", "MASSACHUSETTS": "MA", "PUERTO RICO": "PR", "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD", "NEW MEXICO": "NM", "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO", "Armed Forces Middle East": "AE", "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI", "WEST VIRGINIA": "WV", "WASHINGTON": "WA", "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI", "MARSHALL ISLANDS": "MH", "WYOMING": "WY", "OHIO": "OH", "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV", "LOUISIANA": "LA", "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI", "NORTH DAKOTA": "ND", "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK", "KENTUCKY": "KY", "RHODE ISLAND": "RI", "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR", "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"}


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
    state_score = {}
    for s in sent_dict_file:
        term, score = s.split('\t')
        scores[term] = int(score)
    for t in target_file:
        tweet = json.loads(t)
        # only process if the line is a tweet.
        if ("text" in tweet) and ("place" in tweet) and (tweet["place"] is not None):
            place = tweet["place"]
            if ("country_code" in place) and (place["country_code"] == "US") and ("full_name" in place):
                if place["full_name"] is not None:
                    # print tweet
                    words = tweet["text"].split()
                    line_score = 0
                    # score the line:
                    for w in words:
                        if w in scores:
                            line_score = line_score + scores[w]

                    # get the state code:
                    if place["full_name"].split(',')[1].strip() == "USA":
                        state = place["full_name"].split(',')[0].strip()
                        state = state_to_code[state.upper()]
                    else:
                        state = place["full_name"].split(',')[1].strip()
                    #print "|%s|%d" % (state, line_score)

                    # aggregate:
                    if len(state) == 2:
                        if state in state_score:
                            state_score[state] = state_score[state] + line_score
                        else:
                            state_score[state] = line_score
    
    #print state_score
    
    for w in sorted(state_score, key=state_score.get, reverse=True):
        print w
        return


if __name__ == '__main__':
    main()
