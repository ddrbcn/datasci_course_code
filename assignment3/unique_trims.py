import MapReduce
import sys

"""
Unique trimmed nucleotide Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    key = record[1]
    value = 1
    
    key=key[:-10]

    
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: names tuple
    
    mr.emit(key)
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
