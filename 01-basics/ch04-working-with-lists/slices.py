pizza_styles = [
    "Chicago Deep Dish",
    "New York Style",
    "Detroit Style",
    "Sicilian",
    "Neapolitan",
    "St. Louis Style",
    "Grandma Pizza",
    "Roman Pizza",
    "Tavern Style",
    "California Style"
]

    


# Print the message: The first three items in the list are: Then use a slice to print the first three items from that program's list. 

first_three_items = pizza_styles[:3]
print("\nThe first three items in the list are:")
for pizza in first_three_items:
    print(pizza)

print("\n")

# Print the message: Three items from the middle of the list are: Use a slice to print three items from the middle of the list. 

middle_three_items = pizza_styles[4:7]
print("Three items from the middle of the list are:")
for middle_pizzas in middle_three_items:
    print(middle_pizzas)


print("\n")

# Print the message: The last three items in the list are: Use a slice to print hte last three items in the list

last_three_items = pizza_styles[7:]
print("The last three items in the list are:")
for last_pizza in last_three_items:
    print(last_pizza)

print("\n")

# Make a copy of the list of pizzas, and call it friend_pizza
friend_pizza = pizza_styles[:]

# Add a new pizza to the original list. 
pizza_styles.append("New Haven Style")

print("The original list is:")
for original_pizza in pizza_styles:
    print(original_pizza)
print("\n")

# Add a new pizza to the friend pizza
friend_pizza.append("Quad Cities Pizza")
print("The friend pizza list:")
for friend in friend_pizza:
    print(friend)

