
What I did till can be majorly broken into two parts:

1. To make dictionary for Apache cTAKES
2. Use the extracted terms and look-up using Lucene to get the HPO code

For first I wrote python code (getDictionary.py) to build the dictionary (dictionary1.csv) and the file to be indexed using Lucene for later search (indexing.csv). This codes reads data from hp.obo file 

Second one is a java code having four methods. First it loads the terms from indexing.csv file. Second it creates the index-directory using Lucene. Third it reads from the file.txt (which holds the extracted terms from cTAKES) and Fourth one searches for the term.

The Workflow:

Need to change cTAKES_HOME/desc/ctakes-dictionary-lookup/desc/analysis_engine/DictionaryLookupAnnotatorCSV.xml to include dictionary1.csv

Change cTAKES_HOME/desc/ctakes-clinical-pipeline/desc/analysis_engine/AggregatePlainTextProcessor.xml to use DictionaryLookupAnnotatorCSV.xml as the dictionary Annotator

Also change cTAKES_HOME/resources/org/apache/ctakes/dictionary/lookup/LookupDesc_csv_sample.xml as given. 

The input test data can be obtained from omim.org.

Now the extracted terms were manually written in the file.txt (integration of cTAKES to automatically pass the extracted terms was left) and then searched for using Lucene.
