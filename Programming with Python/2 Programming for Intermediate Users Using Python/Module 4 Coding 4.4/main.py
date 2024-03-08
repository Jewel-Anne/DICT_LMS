# Instructions:
# Create your very own program using these steps.
# 1.) Create a new .py file titled "functionfile."
# This file will serve as your module later on.
# 2.) In your functionfile.py, define at least 5 functions.
# 3.) Go to your main.py
# 4.) From your functionfile, import 2 functions.
# 5.) Use the functions you imported and
# print it on the console

import os

if os.path.exists("functionfile.py"):
    print("Welcome!")
else:
    my_module = open("functionfile.py", "x")
    my_module.close()

from functionfile import func1, func5

func1("Juan Dela Cruz")
func5("singing")