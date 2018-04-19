class MyList:
    def __init__(self):
        self.itemFreq = {}

    def addList(self, inputList):
        for ele in inputList:
            if ele in self.itemFreq:
                self.itemFreq[ele] += 1
            else:
                self.itemFreq[ele] = 1

    def getUnique(self):
        return self.itemFreq.keys()

    def getFreqAll(self):
        return self.itemFreq

    def add(self, element):
        if element in self.itemFreq:
            self.itemFreq[element] += 1
        else:
            self.itemFreq[element] = 1
