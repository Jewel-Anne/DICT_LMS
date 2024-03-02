# Instructions:
# Consider the following variables:
#   my_age = 22
#   mom_age = 61
#   sister_age = 29
# Use the specified operators and the print() function to get a true or false result.
# 1.) And operator (mom_age < sister_age, my_age == 22)
# 2.) Equal operator (mom_age, 61)
# 3.) Or operator (mom_age > 34, sister_age == 22)
# 4.) Greater than or equal to (mom_age, 54)
# 5.) Not operator (sister_age <= 400, my_age ==22)

#########################################################
my_age = 22
mom_age = 61
sister_age = 29

# 1.) And operator (mom_age < sister_age, my_age == 22)
print(mom_age < sister_age and my_age == 22)

# 2.) Equal operator (mom_age, 61)
print(mom_age == 61)

# 3.) Or operator (mom_age > 34, sister_age == 22)
print(mom_age > 34 or sister_age == 22)

# 4.) Greater than or equal to (mom_age, 54)
print(mom_age >= 54)

# 5.) Not operator (sister_age <= 400, my_age ==22)
print(not(sister_age <= 400 and my_age ==22))