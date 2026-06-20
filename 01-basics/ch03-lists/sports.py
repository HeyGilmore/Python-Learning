sports = ['basketball', 'tennis', 'soccer']

# Modifying the list
print(f"\nOriginal List: {sports}")
sports[1] = 'bowling'
print(f"New List: {sports}\n")


# adding new item 
print(f"Original List: {sports}")
sports.append("tennis")
sports.append('golf')
print(f"New List: {sports}\n")

# Inserting an element in the list
print(f"Original List: {sports}")
sports.insert(0,'football')
sports.insert(2,'kickball')
print(f"New List: {sports}\n")

# Deleting Elements from list
print(f"Original List: {sports}")
del sports[0]
print(f"New List: {sports}")
del sports[-1]
print(f"New List: {sports}")
del sports[2]
print(f"New List: {sports}\n")

# Using pop()
print('.pop()')
print(f"Original List: {sports}")
sports.pop()
print(f"Popped List: {sports}")
sports.pop(1)
print(f"2nd Popped List: {sports}\n")


# Adding some elements to my list
sports.append("tennis")
sports.append('golf')
sports.append('kickball')
sports.append('tennis')
sports.append('bowling')
print(f"New Appended List: {sports}")
sports.remove('tennis')
print(f"Taking off tennis: {sports}\n")

# Organize List
print(f"Original List: {sports}")
print(f"Sorted List: {sorted(sports)}")
sports.reverse()
print(f"Reverse List: {sports}\n")


# Organizing the list - PERMANENTLY 
print(f"Original List: {sports}")
sports.sort()
print(f"Sorted List: {sports}")
sports.sort(reverse=True)
print(f"Reverse Sorted List: {sports}\n")

# Count of elemenets in list
print(f"How many elements in the List: {len(sports)}")



