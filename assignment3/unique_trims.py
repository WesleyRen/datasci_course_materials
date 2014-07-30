import MapReduce
import sys

"""
Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

Each input record is a 2 element list [sequence id, nucleotides] where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides

The output from the reduce function should be the unique trimmed nucleotide strings.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    p1 = record[0]
    p2 = record[1][:-10]
    mr.emit_intermediate(p2,1)

def reducer(key, list_of_values):
    #print key
    #print list_of_values
    mr.emit((key))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
