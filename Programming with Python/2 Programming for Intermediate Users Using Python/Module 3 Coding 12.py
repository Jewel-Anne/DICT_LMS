# Instructions:
# Consider the following codes.
# Then, follow the instructions provided below.
#   1.) x = 500
# Note: x should not be bigger than 100.
# Raise an exception that would result in an error
# if x is bigger than 100

x = 500

if x > 100:
    raise Exception("The number should not be bigger than 100")

# Instructions:
#   2.) print(variable_1)
# Note: variable_1 is not defined.
# Throw an exception to make a note of this
# using the try and except block.

try:
    print(variable_1)
except:
    print("Please define the variable")

# Instructions:
#   3.) for i in range(6)
#            print(I'm so happy!)
# Note: The code resulted in a SyntaxError.
# How do we correct this?

for i in range(6):
    print("I'm so happy!") # we should correct by using quotations

# Instructions:
#   4.) print(12*6)
# Note: Using the else keyword, set a conditional statement
# letting the users know if the operation can be performed or not.

try:
    print(12*6)
except:
    print("The operation cannot be performed.")
else:
    print("The operation can be performed.")

# Instructions:
#   5.) best_burger = "Burger King"
#       number_2_burger = "McDonald's"
# Note: How do we make our dode result in an AssertionError?

best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert best_burger == "McDonald's"