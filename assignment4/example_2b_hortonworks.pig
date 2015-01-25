register ./myudfs.jar

-- load the test file into Pig
raw = LOAD './btc-2010-chunk-000' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);


-- load csetest into ntriples
--ntriples = LOAD 'csetest' using org.apache.hcatalog.pig.HCatLoader();

--group the n-triples by object column
objects = group ntriples by (subject);

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subject = foreach objects generate flatten($0), COUNT($1) as count;

--group the count_by_subject by count column
counts = group count_by_subject by (count);


hist = foreach counts generate flatten($0), COUNT($1) as freq;

DUMP hist
