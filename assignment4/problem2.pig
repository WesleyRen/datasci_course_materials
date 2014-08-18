register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the file into Pig
#raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray); 
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the subjects out (because group by produces a tuple of each subject
-- in the first column, and we want each subject ot be a string, not a tuple),
-- and count the number of tuples associated with each subject
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;
counts = group count_by_subject by (count) PARALLEL 50;
hist_of_counts = foreach counts generate flatten($0) as count, COUNT($1) as count_of_count PARALLEL 50;

--order the resulting tuples by their count in descending order
hist_of_counts_ordered = order hist_of_counts by (count)  PARALLEL 50;

-- store the results in the folder /user/hadoop/example-results
-- store hist_of_counts_ordered into '/tmp/p2-results' using PigStorage();
   store hist_of_counts_ordered into '/user/hadoop/p2-results' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_subject_ordered into 's3n://superman/example-results';
-- copy directory from hdfs to a local dir:
--  hadoop fs -copyToLocal /user/hadoop/p2-results p2-results
