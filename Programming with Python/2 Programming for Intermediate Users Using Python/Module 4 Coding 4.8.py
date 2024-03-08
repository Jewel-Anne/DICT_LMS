# Instructions:
# 1.) Browse through the built-in modules in Python
# using the help() function.
# 2.) Select one module. You can also use the help()
# function to know more about the module.
# You can also read up on its documentation at
# https://docs.python.org/3/py-modindex.html
# 3.) Import the module.
# 4.) Learn more about its attributes by applying them to your Python project.

help("modules")

help("random")

from random import normalvariate

rand = normalvariate(mu=5.2, sigma=1.0)
print(rand)