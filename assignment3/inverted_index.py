import MapReduce
import sys

"""
Inverted index from document id, string -> word, document id.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: words in document string
    # value: document identifier
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of doc id
    all_doc = []
    for v in list_of_values:
        if v not in all_doc:
            all_doc.append(v)
    mr.emit((key, all_doc))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
