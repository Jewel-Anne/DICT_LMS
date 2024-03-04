# Instructions:
# Your new cafe, "Coffee Palace," is an instant hit.
# Customers are pouring in and out every minute!
# Sometimes it gets so busy that it's hard to man the cash register.
# You're desperate for a way to make your job easier.
# Fortunately, you're beginning to recognize some regular
# customers who order the same things everyday.
# Maybe that would save ordering and preparation time.
#   1.) Create a class called "Customers."
#   2.) Take note of the following information:
#------------------------------------------------------------------
# | Name    | Beverage               | Food              | Total |
#------------------------------------------------------------------
# | Nate    | Espresso               | Pastrami on rye   | 220   |
# | Elaine  | Strawberry frappuccino | Tuna wrap         | 270   |
# | Samirah | Iced caffe latte       | Cinnamon roll     | 225   |
# | Jerry   | Caramel macchiato      | Glazed doughnut   | 230   |
# | Paz     | Iced tea               | Blueberry pancakes| 315   |
#------------------------------------------------------------------
#   3.) Create a class variable named "greeting,"
#       with the value "Welcome to Coffee Palace!"
#   4.) Use the def keyword and the init method.
#   5.) Create an instance variable named "c_1,"
#       (then "c_2," and so on) for each customer.
#   6.) Type print(Customers.greeting)
#   7.) Looks like Elaine and Jerry are the first to show up!
#       To take their order, print all their information on the console.

class Customers:
    greeting = "Welcome to Coffee Palace!"

    def __init__(self, name, beverage,food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customers.greeting + "\n")

print("Name: " + c_2.name)
print("Beverage: " + c_2.beverage)
print("Food: " + c_2.food)
print("Total Price: " + str(c_2.total) + "\n")

print("Name: " + c_4.name)
print("Beverage: " + c_4.beverage)
print("Food: " + c_4.food)
print("Total Price: " + str(c_4.total))