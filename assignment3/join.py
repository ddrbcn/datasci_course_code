import MapReduce
import sys

"""
SQL Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    value = record
    
    mr.emit_intermediate(key, record)

def reducer(key, list_of_records):
    # key: order_id
    # join: join records
    items = []
    orders = []
    
    for rec in list_of_records:
        #print len(rec)        
        if rec[0] == 'order':
            
            orders.append(rec)
            
        else:
            items.append(rec)
            
    
    for order in orders:
         
        for item in items:
            print len(order), len(item)
            join = list([])
            join = list(order)
            join.extend(item)
            print 'join: ', len(join)

             
            mr.emit(join)
           
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
