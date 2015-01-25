import sys
import json
import random
import time

def hw(sent_file, tweet_file):
    afinnfile = sent_file 
    ouputfile = tweet_file
    tweet_score = 0
    tweets = []
    tweets_scores = []
    tweets_counter = 0
    new_terms = {}
    new_terms_scores = {}
    scores = {} # initialize an empty dictionary

    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited."\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    #print scores.items() # Print every (term, score) pair in the dictionary

    
    
    for line in ouputfile.readlines():
        
        pyresponse = json.loads(line)
        if 'text' in line:
            
            tweet_score = 0
            text = pyresponse['text']
            string_list  = text.split()  # Each line is space-delimited."
            tweets.append(string_list)

            for string in string_list:
                if scores.has_key(string):
                    tweet_score += scores[string]
                elif new_terms.has_key(string):
                    new_terms[string] += 1
                else:
                     new_terms[string] = 1
                     new_terms_scores[string] = 0
                    
            
            tweets_scores.append(tweet_score)
            
            tweets_counter += 1

    '''for key, value in new_terms_scores.iteritems():
        print key, value'''
    #time.sleep(5)
    for term in new_terms:
        tweets_counter = 0
        

        for tweet in tweets:
            
            if term in tweet:
                
                #random_term = term
                #while not scores.has_key(random_term):
                #random_term = random.choice(tweet)
                new_terms_scores[term] += (tweets_scores[tweets_counter]/len(tweet))
                #print tweets_counter, tweets_scores[tweets_counter], len(tweet)
            tweets_counter += 1                    
        new_terms_scores[term] = new_terms_scores[term]/new_terms[term]
    '''for key, value in new_terms_scores.iteritems():
        print key, value'''
    #time.sleep(5)     
    scores.update(new_terms_scores)
    for key, value in new_terms_scores.iteritems():
        
        key = key.strip()
        key = key.strip('\t')
        key.replace('\t','_')
        key.replace(' ','_')
        print key, str(value)

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    

if __name__ == '__main__':
    main()
