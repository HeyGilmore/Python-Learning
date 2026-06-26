movies = [
    "the matrix",
    "inception",
    "interstellar",
    "the dark knight",
    "forrest gump",
    "pulp fiction",
    "the godfather",
    "spider-man: into the spider-verse",
    "jurassic park",
    "back to the future"
]

requested_movies = [
    "pulp fiction",
    "interstellar", 
    "school of rock"
]


# Check if list is empty
if not movies:
    print("No movies avaiable")
else:
    # Loop through list
    for mov in movies:
        # Check if forrest gump
        if mov == "forrest gump":
            print(f"We are out of {mov} at this time")
        else:
            print(f"In stock: {mov}")

print("\n")

for requested in requested_movies:
    if requested in movies:
        print(f"In Stock: {requested}")
    else:
        print(f"Out of Stock: {requested}")
