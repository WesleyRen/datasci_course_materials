import MapReduce
import sys

"""
Inverted index from document id, string -> word, document id.
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: words in document string
    # value: document identifier
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of doc id
    for v in list_of_values:
        if v[0] == 'order':
            for e in v:
                order = v;
    for v in list_of_values:
        if v[0] == 'line_item':
            mr.emit(order+v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)