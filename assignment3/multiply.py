import MapReduce
import sys

"""
Matrix product Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: final matrix index
    # value: elements product
    #record: [matrix, i, j, value]
    print record
    
    if record[0] == 'a':
        for k in range(5):
            mr.emit_intermediate((record[1], k), [record[2], record[3]])
            
    else:
        for k in range(5):
            mr.emit_intermediate((k, record[2]), [record[1], record[3]])    
   
    
    
    
    

def reducer(key, list_of_values):
    # key: matrix elements factors
    print key, list_of_values
    product = 0
    for v in range(len(list_of_values)):
        for v1 in range(v+1,len(list_of_values)):
            print list_of_values[v][0], list_of_values[v1][0]
            if list_of_values[v][0] == list_of_values[v1][0]:
                product = product + list_of_values[v][1]*list_of_values[v1][1]
                print product    

    mr.emit((key[0],key[1],product ))
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
