# Operators are of many types

# 1 Arithmetic Operator
# 2 Assignment Operator
# 3 Comparison Operator
# 4 Logical Operator
# 5 Bitwise Operator
# 6 Membership Operator
# 7 Identity Operator


# Arithmetic Operators Perform
# 1 Addition           (+)
# 2 Subtraction        (-)
# 3 Multiplication     (*)
# 4 Division           (/)
# 5 Modulus            (%)
# 6 Exponentiation     (**)
# 7 Floor Division     (//)

# Arithmetic Operator
a = 10
b = 20

print("Addition:", a + b)              # Addition: 30
print("Subtraction:", a - b)           # Subtraction: -10
print("Multiplication:", a * b)        # Multiplication: 200
print("Division:", a / b)              # Division: 0.5
print("Modulus:", a % b)               # Modulus: 10
print("Exponentiation:", a ** b)       # Exponentiation: 100000000000000000000
print("Floor Division:", a // b)       # Floor Division: 0


# Comparison Operators Perform
# 1 Equal              (==)
# 2 Not Equal          (!=)
# 3 Greater Than       (>)
# 4 Less Than          (<)
# 5 Greater Than Equal (>=)
# 6 Less Than Equal    (<=)

a = 20
b = 18

print("Equal:", a == b)                # Equal: False
print("Not Equal:", a != b)            # Not Equal: True
print("Greater Than:", a > b)          # Greater Than: True
print("Less Than:", a < b)             # Less Than: False
print("Greater Than Equal:", a >= b)   # Greater Than Equal: True
print("Less Than Equal:", a <= b)      # Less Than Equal: False


# Logical Operators
# AND   (and)
# OR    (or)
# NOT   (not)

a = 50
b = 70

print("AND Operator:", a > 10 and b > 50)   # AND Operator: True
print("OR Operator:", a > 10 or b < 80)    # OR Operator: True
print("NOT Operator:", not a > 20)         # NOT Operator: False


# Membership Operators
# 1 in
# 2 not in

lst = [20, 30, 70, 80, 79]

print("in operator:", 30 in lst)           # in operator: True
print("in operator:", 100 in lst)          # in operator: False
print("not in operator:", 30 not in lst)   # not in operator: False
print("not in operator:", 100 not in lst)  # not in operator: True


# Identity Operators
# 1 is
# 2 is not

a = 10
b = 10

print(a is b)                              # True
print(a is not b)                          # False
