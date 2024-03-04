# Instructions:
# 1.) Create a base class called ClubMembers.
# 2.) Using the init method, add the following properties:
# name, birthday, age, favorite food, and goal.
# 3.) Define a method that will display or print all the 5 properties.
# Include the parameter self." (Hint: Use the print() function!)
# 4.) Next, create a subclass called ClubOfficers.
# 5.) Then add a new property: position by overriding the
# init method of the base class ClubMembers.
# 6.) Include a method that will display or print all the 6 properties.
# (Hint: Make sure it's different from the previous method you defined.)
# 7.) The Cooking Club got a new member!
# This is what he wrote on his application:
#       Name: Tom
#       Birthday: January 16
#       Age: 14
#       Favorite Food: Ice cream
#       Goal: To be happy
# 8.) Create an object and name it m_1.
# 9.) Elections are finally over! Vera won for class treasurer.
# Here are her details:
#       Name: Vera
#       Birthday: June 22
#       Age: 16
#       Favorite Food: Beef stroganoff
#       Goal: To be the world's greatest chef
#       Position: Treasurer
# 10.) Create an object and name it o_4.
# 11.) Call the methods that will display the
# details of the new member Tom and the new Treasurer, Vera.
# 12.) Your console should look like:
#       Name: Tom
#       Birthday: January 16
#       Age: 14
#       Favorite Food: Ice cream
#       Goal: To be happy
#       Name: Vera
#       Birthday: June 22
#       Age: 16
#       Favorite Food: Beef stroganoff
#       Goal: To be the world's greatest chef
#       Position: Treasurer
#
#       Process finished with exit code 0

class ClubMembers:
    def __init__(self, name, birthday, age, food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.food = food
        self.goal = goal

    def display(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite food: ", self.food)
        print("Goal: ", self.goal)

class ClubOfficers (ClubMembers):
    def __init__(self, name, birthday, age, food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, food, goal)

    def display1(self):
        super().display()
        print("Position: ", self.position)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display()
o_4.display1()