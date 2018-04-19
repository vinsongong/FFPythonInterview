import numbers

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

"""
Problem 3:
Reformatting this code to be more elegant
    abc = ['dog', 'Fido', 10]
    animal = abc[0]
    name = abc[1]
    age = abc[2]
    output = ('{name} the {animal} is {age} years old'.format(
    animal=animal, name=name, age=age))
"""
def reformattedProblem3():
    animal, name, age = ['dog', 'Fido', 10]
    output = ('{name} the {animal} is {age} years old'
        .format(animal=animal, name=name, age=age))
    return output
