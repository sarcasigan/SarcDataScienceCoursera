import MapReduce
import sys

currentrow = 0
currentcol = 0
currentk = 0

mr = MapReduce.MapReduce()

def mapper(record):   
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]     
    if matrix == "a":
        if i != currentrow:
            currentk += 1
            currentrow = i
        if currentk > 4:
            currentk = 0
        mr.emit_intermediate((i,currentk), value)
    if matrix == "b":
        if j != currentcol:
            currentk += 1
            currentcol = j
        if currentk > 4:
            currentk = 0
        mr.emit_intermediate((j, currentk), value)

def reducer(key, list_of_values):            
    for items in list_of_values:
        print key, items

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
