import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):    
    friendA = record[0]    
    friendB = record[1]    
    record2 = [friendB, friendA]
    mr.emit_intermediate(friendA, " ".join(record))
    mr.emit_intermediate(friendB, " ".join(record2))    

def reducer(key, list_of_values):        
    newlist = list_of_values
    seen = set()
    for friendlist in list_of_values: 
        if friendlist in seen:            
            newlist = filter(lambda a: a != friendlist, newlist)            
        else:            
            seen.add(friendlist)             
    for v in newlist:
        mr.emit((key, v.split()[1]))                          

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
