# 1. First, we ask the user to input a list of names, separated by commas.
# 2. Next, we split the string into a list of strings.
# 3. Then, we find the length of the list.
# 4. Finally, we generate a random number between 0 and the length of the list.
# 5. We use that random number to select a name from the list.
# 6. We print out the name that was selected.
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
who_will_pay = names[random_choice]
print(who_will_pay + " is going to buy the meal.")
