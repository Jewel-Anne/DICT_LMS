# Instructions:
# You use a shopping list when you're buying groceries.
#   groceries = {"chicken":8, "apples":6, "cucumbers":3, "milk":2, "oranges":4}
# So far you already have the oranges.
# Use the .pop method to cross out the item that's already in your cart.

groceries = {"chicken": 8, "apples": 6, "cucumbers": 3, "milk": 2, "oranges": 4}

groceries.pop("oranges")
print(groceries)

# Instructions:
# Consider this dictionary:
#   speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}
# You're interested in looking up the speakers' names so you can check their research.
# You're not very interested in their age. Use the .keys() method t keep a list of their names.

speakers = {"Sir Rafael": 54, "Ms. Joan": 33, "Ms. Dana": 67}

name_only = speakers.keys()
print(name_only)

# Instructions:
# Here's the result of the swimming team tryout:
#   Carl(passed), Quentin(failed), John Y.(passed), Peter(failed), Max T.(passed),
#   Joseph(passed), Jone(failed), Jorge(failed), George(passed), Ben(passed),
#   Jerome(passed), Rick(failed), Max G.(failed),John P.(failed), and Vince(passed).
# You're in a hurry to read through all those names,
# but you want to know if your best friend Jorge passed the tryouts.
# Use the .get() method to find out.

tryout = {"Carl": "passed", "Quentin": "failed", "John Y.": "passed", "Peter": "failed", "Max T.": "passed",
        "Joseph": "passed", "Jone": "failed", "Jorge": "failed", "George": "passed", "Ben": "passed",
        "Jerome": "passed", "Rick": "failed", "Max G.": "failed", "John P.": "failed", "Vince": "passed"}
print(tryout.get("Jorge"))