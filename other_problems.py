"""
Problem 2:
Takes string as input. Output to be int/float/string depending
if the string can be converted to float or integer type
"""
def convert(input):
    if type(input) != type(""):
        raise TypeError("convert() expected input of " + str(type(''))
        + " but was provided input of " + str(type(input)))
    try:
        floatVal = float(input)
        if '.' not in input:
            return int(floatVal)
        return floatVal
    except ValueError:
        return input
