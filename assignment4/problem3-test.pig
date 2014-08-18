register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray); 
#raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);
busTriples = FILTER ntriples BY (subject matches '.*business.*');
#store busTriples into '/tmp/p3-results' using PigStorage();
busTriples2 = foreach busTriples generate subject as subject2, predicate as predicate2, object as object2;
#store busTriples2 into '/tmp/p3-results' using PigStorage();

sextuples = JOIN busTriples by subject, busTriples2 by subject2;
#store sextuples into '/tmp/p3-results' using PigStorage();

sextuples2 = DISTINCT sextuples;

#store sextuples2 into '/user/hadoop/p3-results' using PigStorage();
store sextuples2 into '/tmp/p3-results' using PigStorage();
