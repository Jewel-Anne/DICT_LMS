# Instructions:
# 1.) Create a new .txt file.
# Use the "w" mode.
# 2.) Answer the question: "What do I like about learning Python?"
# in 1 sentence.
# 3.) This time, let's use the "a" mode to add to your file.
# Answer the following questions (1 sentence each):
#   "What do I plan to do after learning Python?"
#   "How do I apply what I've learned?"
#   "What are my goals?"
# Tip: Use \n, or newline to create a new line of code.
# In this case, it will work as paragraphs.
#       f.write("\nProgramming is cool!")
# 4.) use "r" mode to read your file.
# 5.) Use the close() function to close your file.

module3coding4 = open("module3coding4.txt", "w")
module3coding4.write("I like learning Python because it's fun!")

module3coding4 = open("module3coding4.txt", "a")
module3coding4.write("\nI plan to learn machine learning after.")
module3coding4.write("\nI'll apply what I've learned by teaching others.")
module3coding4.write("\nMy goal is to be a good python programmer.")

module3coding4 = open("module3coding4.txt", "r")
module3coding4.close()