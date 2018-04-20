from Tkinter import *
import json

labels = ["City", "County", "Latitude", "Longitude"]

class CityInformation:
    def __init__(self, top, labels, cities, jsonData):
        self.jsonData = jsonData
        self.entries = {}
        variable = StringVar(top)
        variable.set("Choose a city...") # default value for OptionMenu
        for i, label in enumerate(labels):
            row = Frame(top)
            labelObj = Label(row, width=15, text=label, anchor='w')
            if i == 0:
                entry = OptionMenu(row, variable, *cities, command=self._updateInfo)
            else:
                entry = Entry(row, state='disabled')
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            labelObj.pack(side=LEFT)
            entry.pack(side=RIGHT, expand=YES, fill=X)
            self.entries[label] = entry

    def _updateInfo(self, city):
        for row in self.jsonData:
            if row['name'] == city:
                self._updateInfoHelper(row)

    def _updateInfoHelper(self, row):
        entryDict = {'County': 'full_county_name',
                     'Latitude': 'primary_latitude',
                     'Longitude': 'primary_longitude'}
        for label, jsonKey in entryDict.iteritems():
            entry = self.entries[label]
            entry.config(state='normal')
            entry.delete(0, END)
            entry.insert(0, row[jsonKey])
            entry.config(state='disabled')

def parseJson(fileName):
    cityNames = []
    data = json.load(open(fileName))
    for row in data:
        if(row['full_county_name']):
            cityNames.append(row['name'])
    return sorted(cityNames), data

def main():
    top = Tk()
    top.title('City Information')
    cities, jsonData = parseJson('ca.json')
    CityInformation(top, labels, cities, jsonData)
    top.mainloop()

if __name__ == "__main__":
    main()
