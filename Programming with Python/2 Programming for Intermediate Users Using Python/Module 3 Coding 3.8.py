# Note:
# If you're a PyCharm user,
# you'll need to open a new .py file for this exercise
# (but please use the same Python project).
#
# If you're a Google Colab user,
# use the same notebook from the previous exercise.
# (Do not delete the code from the previous exercise.)
#
# Instructions:
# 1.) Open the .txt file you created in the previous coding exercise.
# This time, use the "r" mode.
# 2.) Use the print() function and the read() mode to view the
# contents of the file on the console.
# 3.) Use the readline() method to read only a single line.
# 4.) Next, let's try using the for loops.
# 5.) Lastly, let's delete the file.

# PREVIOUS CODE:
module3coding8 = open("module3coding8.txt", "w")
module3coding8.write("I like learning Python because it's fun!")

module3coding8 = open("module3coding8.txt", "a")
module3coding8.write("\nI plan to learn machine learning after.")
module3coding8.write("\nI'll apply what I've learned by teaching others.")
module3coding8.write("\nMy goal is to be a good python programmer.")

module3coding8 = open("module3coding8.txt", "r")
module3coding8.close()

# CODING EXERCISE 3.8:
    # using read()
module3coding8 = open("module3coding8.txt", "r")
print(module3coding8.read())
module3coding8.close()

    # using readline()
module3coding8 = open("module3coding8.txt", "r")
print(module3coding8.readline())
module3coding8.close()

    # using for loop to read each line
module3coding8 = open("module3coding8.txt", "r")
for x in module3coding8:
    print(x)
module3coding8.close()

    # deleting file
import os
if os.path.exists("module3coding8.txt"):
    os.remove("module3coding8.txt")
    print("File successfully deleted!")
else:
    print("File does not exist.")
