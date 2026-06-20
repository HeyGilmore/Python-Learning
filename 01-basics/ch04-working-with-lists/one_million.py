
# Make a list of the number from one to one million, and then use a for loop to print the numers. 
numbers = [num for num in list(range(1,1_000_001))]
# print(f"{numbers}")

# Make a list of the numbers from one to one million, and then use min, max, to see where it starts and ends, then use sum to see how quickly python can add a million numbers. 
print(f"Max Number: {max(numbers)}")
print(f"Min Number: {min(numbers)}")
print(f"Sum of Number: {sum(numbers)}")
