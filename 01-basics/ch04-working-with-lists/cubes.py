# a number raised to the third power is caled a cube. Make a list of the first 10 cubes and use a for loop to print out the value of each cube. 

cubes = list(range(1,11))
for cube in cubes:
    print(f"{cube**3}")


comprehension_cubes = [cube**3 for cube in range(1,11)]
print(comprehension_cubes)

