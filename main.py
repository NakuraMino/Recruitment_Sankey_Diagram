import CSVParser

parser = CSVParser.CSVParser()

parser.parseCSV("test/test.csv")
parser.printCounts()
parser.addAggregatesToResultsJS("resultsTest")