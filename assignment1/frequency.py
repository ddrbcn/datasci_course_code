import sys
import json
import random
import time

def hw(tweet_file):
    
    ouputfile = tweet_file
    tweet_score = 0
    tweets = []
    tweets_scores = []
    tweets_counter = 0
    freq_terms = {}
    new_terms_scores = {}
    scores = {} # initialize an empty dictionary

    
    #print scores.items() # Print every (term, score) pair in the dictionary

    
    
    for line in ouputfile.readlines():
        
        pyresponse = json.loads(line)
        if 'text' in line:
            
            tweet_score = 0
            text = pyresponse['text']
            string_list  = text.split()  # Each line is space-delimited."
            

            for string in string_list:
                if freq_terms.has_key(string):
                    freq_terms[string] += 1
                else:
                     freq_terms[string] = 1
                     
                    
            
            
    
    for key, value in freq_terms.iteritems():
        
        key = key.strip()
        
        print key, value

def lines(fp):
    print str(len(fp.readlines()))

def main():
    
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    

if __name__ == '__main__':
    main()
