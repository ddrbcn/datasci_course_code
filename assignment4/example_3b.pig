register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- later you will load to other files, example:
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);


--filter in order to consider triples whose subject matches rdfabout.com
filtered = FILTER ntriples BY (subject matches '.*rdfabout\\.com.*');

--duplicate collection
duplicated = FOREACH filtered GENERATE subject as subject2, predicate as predicate2, object as object2;

--join triples
joined = JOIN filtered BY object, duplicated BY subject2;

-- store the results in the folder /user/hadoop/example-results
store joined into '/user/hadoop/example-results' using PigStorage();