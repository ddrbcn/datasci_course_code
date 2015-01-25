import sys
import json

def hw(sent_file, tweet_file):
    
    afinnfile = sent_file 
    ouputfile = tweet_file
    #tweet_scores = open("finalscores.txt", "a")
    tweet_score = 0
    scores = {} # initialize an empty dictionary

    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited."\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    #print scores.items() # Print every (term, score) pair in the dictionary

    
    
    for line in ouputfile:
        
        pyresponse = json.loads(line)
        if 'text' in line:
            tweet_score = 0
            text = pyresponse['text']
            string_list  = text.split()  # Each line is space-delimited."
            for string in string_list:
                if scores.has_key(string):
                    tweet_score += scores[string] 
            print tweet_score
            #tweet_scores.write('%d'%tweet_score)
    #tweet_scores.close()        
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    

if __name__ == '__main__':
    main()
