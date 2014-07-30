import MapReduce
import sys, csv

"""
Inverted index from document id, string -> word, document id.
"""

mr = MapReduce.MapReduce()
outDimensionRows = 0;
outDimensionCols = 0;

def mapper(record):
    matrixName = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if matrixName == "a":
        for k in range(0, outDimensionCols):
            mr.emit_intermediate((row, k), ["a", row, col, val])
    if matrixName == "b":
        for i in range(0, outDimensionRows):
            mr.emit_intermediate((i, col), ["b", row, col, val])

def reducer(key, list_of_values):
    sum = 0;
    # print key
    # print list_of_values
    for v in list_of_values:
        if v[0] == "a":
            for u in list_of_values:
                if u[0] == "b" and v[2] == u[1]:
                    sum = sum + (v[3] * u[3]) 
    mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
  for row in  csv.reader(lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    if row[0].strip('[]"') == "a" and outDimensionRows < int(row[1]):
      outDimensionRows = int(row[1])
    if row[0].strip('[]"') == "b" and outDimensionCols < int(row[2]):
      outDimensionCols = int(row[2])
  outDimensionRows += 1;
  outDimensionCols += 1;

  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
