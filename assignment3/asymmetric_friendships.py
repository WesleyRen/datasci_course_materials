import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    p1 = record[0]
    p2 = record[1]
    v1 = p1+' '+p2
    v2 = p2+' '+p1
    mr.emit_intermediate(v1,1)
    mr.emit_intermediate(v2,1)

def reducer(key, list_of_values):
    #print key
    #print list_of_values
    k = key.split()[0]
    v = key.split()[1]
    sym_count = 0
    for l in list_of_values:
        sym_count += 1;
    if sym_count == 1:
        mr.emit((k,v))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
