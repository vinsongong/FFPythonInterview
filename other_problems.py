import numbers
import operator as oper
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

"""
Problem 4:
Method that takes 3 numbers as input and finds the minimum
of the three without using the built-in min function
"""
def findMin(first, second, third):
    if not (isinstance(first, numbers.Real) \
       and isinstance(second, numbers.Real) \
       and isinstance(third, numbers.Real)):
        raise TypeError("inputs to findMin() must be numbers")

    if first < second and first < third:
        return first
    if second < first and second < third:
        return second
    return third

"""
Problem 5:
Reformatting this code to be more elegant
    def apply_operation(left_operand, right_operand, operator):
        if operator == '+':
            return left_operand + right_operand
        elif operator == '-':
            return left_operand - right_operand
        elif operator == '*':
            return left_operand * right_operand
        elif operator == '/':
            return left_operand / right_operand
"""
def apply_operation(left_operand, right_operand, operator):
    if not (isinstance(left_operand, numbers.Real) \
       and isinstance(right_operand, numbers.Real)):
        raise TypeError("operands of apply_operation() must be numbers")

    if operator not in ['+', '-', '*', '/']:
        raise TypeError("operator of apply_operation() not supported")

    ops = {'+': oper.add,
           '-': oper.sub,
           '*': oper.mul,
           '/': oper.div}
    return ops[operator](left_operand, right_operand)

def main():
    print (apply_operation(3, 4, '*'))

if __name__ == "__main__":
    main()
