names = [
    "Gilmore",
    "Dexter",
    "Maverick",
    "Luna",
    "Atlas",
    "Zelda",
    "Ranger",
    "Nova",
    "Spike",
    "Hazel"
]



#  Doesn't add the last three 
bottom_three = names[:-3]
for name in bottom_three:
    print(name)

print("\n")

# Start after 4th person
start_at_4 = names[4:]
for name in start_at_4:
    print(name)


print("\n")

# Only show the top three 
top_players = names[0:3]

for num, name in enumerate(top_players, start=1):
    print(f"#{num}) {name}")


print("\n")


for num, bottom in enumerate(reversed(names[-3:]),start=1):
    print(f"#{(len(names)+1)-num}) {bottom}")


print("\n")

#  copying the list. 
friend_list = names[:]
for name in friend_list:
    print(name)


