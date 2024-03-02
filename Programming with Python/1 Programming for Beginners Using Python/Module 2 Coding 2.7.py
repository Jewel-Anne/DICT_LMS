# Instructions:
# Using variables and input functions, make a slam book for your users!
# Imagine you're in highschool and you have a lot of friends.
# This is a great opportunity to learn more about them!
# Ask your friends for the following information:
# Name:
# Age:
# Favorite Color:
# Favorite Movie:
# Mobile Number:
# Motto in Life:

print("Welcome to my slam book! Please enter the needed information")
FriendName = input("Name:")
FriendAge = int(input("Age:"))
FriendColor = input("Favorite Color:")
FriendMovie = input("Favorite Movie:")
FriendNumber = int(input("Mobile Number:"))
FriendMotto = input("Motto in Life:")

print("\n#############################")
print("Hello " + FriendName + "!")
print("These are your information:")
print("Your name is " + FriendName)
print("Your age is " + str(FriendAge))
print("Your favorite color is " + FriendColor)
print("Your favorite movie is " + FriendMovie)
print("Your mobile number is " + str(FriendNumber))
print("Your motto in life is " + FriendMotto)
