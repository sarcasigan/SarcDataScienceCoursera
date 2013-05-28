import MapReduce
import sys
import itertools

mr = MapReduce.MapReduce()

def mapper(record):    
    key = record[1]    
    mr.emit_intermediate(key, record)        

def reducer(key, list_of_values): 
    orderlist = list_of_values[0]
    list_of_values.pop(0)
    for newlist in list_of_values:
        mr.emit(list(itertools.chain(*(orderlist, newlist))))                          

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)