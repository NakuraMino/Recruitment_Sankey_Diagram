import csv

class CSVParser:
    """ 
    Parses CSV file and keeps track of aggregate statistics for 
    the last file read. Also outputs information to generate a
    Sankey Diagram
    """

    def __init__(self):
        self.titles = ['Company', 'Role name', 'Applied Date', 
                            'Coding Challenge', 'Recruiter Chat', 'First Round', 
                            'Second Round' , 'Third Round', 'Result']
        self.lastFile = None
        self.initState()
    
    def initState(self):
        """ resets internal statistics
        """
        self.aggregates = {}
        self.counts = {t:0 for t in self.titles[3:]}
        self.counts['Applied'] = 0
        self.counts['Ghosted'] = 0
        self.counts['Accepted'] = 0
        self.counts['Rejected'] = 0
        self.counts['Ongoing'] = 0
        

    def parseCSV(self, filepath):
        """ reads in a csv file and keeps track of the aggregate statistics
            @param filepath: the path to the csv file to read
            @requires file at filepath to exist
        """
        self.initState()
        self.lastFile = filepath
        with open(filepath, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                comp = row[self.titles[1]]
                lastState = "['Applied'"
                if comp == '':
                    pass
                self.counts['Applied'] += 1
                for title in self.titles[3:-1]:
                    state = row[title]
                    if state != '':
                        self.counts[title] += 1
                        lastState += ", '"+ title + "'"
                        if lastState not in self.aggregates:
                            self.aggregates[lastState] = 0
                        self.aggregates[lastState] += 1
                        lastState = "['" + title + "'"                        
                
                # last column has different final states (accepted, ghosted etc.)
                result = row[self.titles[-1]]
                if result == '':
                    self.counts['Ghosted'] += 1
                    lastState += ", 'Ghosted'"
                else:
                    self.counts[result] += 1
                    lastState += ", '" + result + "'"
                if lastState not in self.aggregates:
                    self.aggregates[lastState] = 0
                self.aggregates[lastState] += 1

    def printCounts(self, outFile=None):
        """ prints simple aggregate statistics to stdout (or file if specified)
            @param outFile: path to write file to
        """
        if self.lastFile is None:
            print("no file read: use CSVParser.parseCSV(filepath) to read file")
        
        writer = None
        if outFile is not None:
            writer = open(outFile, "w")
        printer = lambda x: print(x) if writer is None else writer.write(x)
        printer("Applied total: " + str(self.counts['Applied']))
        printer("Coding Challengs total: " + str(self.counts['Coding Challenge']))
        printer("Recruiter Chat total: " + str(self.counts['Recruiter Chat']))
        printer("First Round total: " + str(self.counts['First Round']))
        printer("Second Round total: " + str(self.counts['Second Round']))
        printer("Third Round total: " + str(self.counts['Third Round']))
        printer("Accepted total: " + str(self.counts['Accepted']))
        printer("Ghosted total: " + str(self.counts['Ghosted']))
        printer("Rejected total: " + str(self.counts['Rejected']))
        printer("Ongoing total: " + str(self.counts['Ongoing']))


    def saveAggregates(self, outFilePath):
        """ writes aggregate information to outFilePath in format necessary for Sankey Diagram
            @param outFilePath: path to write file to
        """
        if self.lastFile is None:
            print("no file read: use CSVParser.parseCSV(filepath) to read file")
        with open(outFilePath, "w") as writer:
            for key in self.aggregates:
                writer.write(key + ", " + str(self.aggregates[key]) + "],\n")

    def addAggregatesToResultsJS(self, resultName):
        with open("results.js", "a") as writer:
            writer.write("\n")
            writer.write(resultName + " = [")
            for key in self.aggregates:
                writer.write(key + ", " + str(self.aggregates[key]) + "],\n")
            writer.write("]")
