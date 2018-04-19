class MyList:
    def __init__(self):
        self.itemFreq = {}

    # Adds input list of items to dictionary
    def addList(self, inputList):
        for item in inputList:
            if item in self.itemFreq:
                self.itemFreq[item] += 1
            else:
                self.itemFreq[item] = 1

    # Returns all the unique items from the dictionary
    def getUnique(self):
        return self.itemFreq.keys()

    # Returns all the items and their frequency from the dictionary
    def getFreqAll(self):
        return self.itemFreq

    # Adds input item to dictionary
    def add(self, item):
        if item in self.itemFreq:
            self.itemFreq[item] += 1
        else:
            self.itemFreq[item] = 1
