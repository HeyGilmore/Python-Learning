

# working with range() to generate a series of numbers
for num in range(1,10):
    print(f"#{num}. Hello World")

#Capable of just adding one number and it starts at 0 ending just before 11
for num in range(11):
    print(f"#{num}.")


# Making a list of numbers
list_of_numbers =list(range(11))
print(f"Whats in the list: {list_of_numbers}\n") 

# How to showcase only even numbers
even_numbers = list(range(0,20,2))
print(f"Showcase Even Numbers: {even_numbers}\n")


# Make a list of the first 10 square numbers
squares = []
for value in range(1,11): 
    squares.append(value ** 2)

print(f"What is the square number from the list: {squares}\n")

# How to find the min, max and sum of all numbers in the list. 
numbers = [42, 17, 89, 3, 56, 71, 24, 95, 11, 68]
print(f"{numbers}")
print(f"Min numbers: {min(numbers)}")
print(f"Max numbers: {max(numbers)}")
print(f"Sum of the numbers: {sum(numbers)}\n")

# Line Comprehension
squaring_numbers = [value**2 for value in range(1,11)]
print(f"Squaring the list: {squaring_numbers}")
