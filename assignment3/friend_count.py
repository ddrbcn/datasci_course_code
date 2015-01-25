import MapReduce
import sys

"""
Social network friend counting Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    
    key = record[0]
    
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_friends):
    # key: name
    # value: list of friends
    total = 0
    for v in list_of_friends:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
