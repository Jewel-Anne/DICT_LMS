# Instructions:
# Your new cafe, "Coffee PLace," is an instant hit.
# Customers are pouring in and out every minute!
# So far, you have two regular customers who seem to love buying from your cafe.
# They show up to breakfast everyday and they always order the same things.
# Using classes, let's try to save their orders!
# 1.) Create a class called "Customers."
# 2.) Take note of the following information:
# ---------------------------------------------------------
# | Name    | Beverage          | Food            | Total |
# ---------------------------------------------------------
# | Samirah | Iced caffe latte  | Cinnamon roll   | 225   |
# | Jerry   | Caramel macchiato | Glazed doughnut | 230   |
# ---------------------------------------------------------
# 3.) Create a class variable named "greeting",
# with the value "Welcome to the Coffee Palace!"
# 4.) Create instance variables for Samirah and Jerry. (ex. c_1)
# 5.) Include the attributes listed on the table. (ex. c_1.name)
# 6.) Type print(Customers.greeting)
# 7.) What does Samirah want to drink? Print her beverage on the console.
# 8.) What does Jerry want to eat? Print his food on the console.

class Customers:
    greeting = "Welcome to the Coffee Palace!"

c_1 = Customers()
c_1.name = "Samirah"
c_1.beverage = "Iced caffe latte"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "Caramel macchiato"
c_2.food = "Glazed doughnut"
c_2.total = 230

print(Customers.greeting)
print("Samirah wants to drink " + c_1.beverage)
print("Jerry wants to eat " + c_2.food)