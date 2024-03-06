# Instructions:
# Consider the table below
# --------------------------------------------
# | Flavor           | Toppings              |
# --------------------------------------------
# | vanilla          | almonds               |
# | chocolate        | banana slices         |
# | strawberry       | chocolate syrup       |
# | cookies n' cream | caramel syrup         |
# | bubblegum        | white chocolate chips |
# --------------------------------------------
# 1.) Make two lists: one for flavors and one for toppings.
# 2.) Using the .zip() function and dict() function, combine the
# two lists into one dictionary names ice_cream.
# 3.) Use the print() function to print the ice_cream dictionary.
# 4.) Overwrite the value of the chocolate ice crea. Change
# "banana slices" to "blueberries"
# 5.) Surprise!
# There are two new ice cream flavors (matcha and ube)
# and two new toppings (pistachios and mango slices).
# Use the .update method to add these new flavors and toppings
# 6.) Use the print function to print both the new value of
# chocolate and the updated ice_cream dictionary.

flavors = ["vanilla", "chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]

ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({'matcha': 'pistachios', 'ube': 'mango slices'})
print(ice_cream)