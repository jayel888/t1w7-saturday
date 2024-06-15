import math_ops

num1 = 5
num2 = 6

result_add = math_ops.add(num1,num2)
print(result_add)

result_subtract = math_ops.subtract(num1, num2)
print(result_subtract)

result_multiply = math_ops.multiply(6,7,2,5)
print(result_multiply)

result_divide = math_ops.divide(6, 3)
print(result_divide)

# Another way to import
print("----------------------------------------")
from math_ops import add, subtract, multiply, divide
result_add = add(num1, num2)
print(result_add)

result_subtract = subtract(7, 3, 5, 7)
print(result_subtract)

# Pythons pre-defined modules
import math, random

num1 = math.pow(2,8)
print(num1)

num2 = math.sqrt(64)
print(num2)

randValue = random.randrange(1,10)
print(randValue)