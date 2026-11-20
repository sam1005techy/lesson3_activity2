# 1) Create variables to store different types of values:

# - `name` as text (string)
name="sanaa"
# - `age` as a whole number (integer)
age=10

# - `is_student` as True/False (boolean)
is_student=False
# - `weight` as a decimal number (float)
weight=5.9
# 2) Print each variable’s value.
print(name)
print(age)
print(is_student)
print(weight)
# 3) Print the datatype of each variable using `type()`.
print(type(name))
print(type(age))
print(type(is_student))
print(type(weight))
# 4) Show a message that type casting will happen next.
print("typecasting")

# 5) Convert `age` from an integer to a string and store it back in `age`.
age=str(age)
# 6) Print `age` and print its datatype again to confirm it changed.
print(age)
print(type(age))
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight=int(weight)
# 8) Print `weight` and print its datatype again to confirm it changed
print(weight)
print(type(weight))