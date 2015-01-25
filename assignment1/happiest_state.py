import sys
import json

def hw(sent_file, tweet_file):
    
    afinnfile = sent_file 
    ouputfile = tweet_file
    #tweet_scores = open("finalscores.txt", "a")
    tweet_score = 0
    scores = {} # initialize an empty dictionary
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
    states_happyness = {}
        
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
            #print tweet_score
            
            if ('place' in line) and not ('"place":null' in line):
                place = pyresponse['place']      
                if place['country_code'] == 'US':
                    #print place['full_name']
                    state = place['full_name'].split(',')
                    state_striped = state[1].strip()
                    #print
                    
                    if (not states_happyness.has_key(state_striped)) and (not states_happyness =='USA'):
                        states_happyness[state_striped] =  tweet_score
                    else:
                        states_happyness[state_striped] +=  tweet_score
    
    print max(states_happyness, key = states_happyness.get)
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    

if __name__ == '__main__':
    main()
