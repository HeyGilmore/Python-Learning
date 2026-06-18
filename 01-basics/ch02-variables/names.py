name = "jordan lawrence"
print(name)

print("Title:",name.title())

print("Upper:",name.upper())
print("Lower:",name.lower())



first_name = "bob"
middle_name = "the"
last_name = "builder"
full_name = f"{first_name} {middle_name} {last_name}"
full_name_second = first_name+" "+ middle_name+" "+last_name
print("First Name:",full_name)
print("First Name Second:",full_name_second)

print(f"Hello {full_name.title()}!")

welcome_banner = f"Hello, {name.title()}"
print("NOTICE: "+welcome_banner)

full_name_format = "{} {} {}".format(first_name, middle_name, last_name)
print("New Format: "+ full_name_format)
 
print("\tthis is one tab\tthis should be a new tab. ")      
print("this is a new line, \nthis is a new line \nthis is a new line")

right_space = "spacing on the right.               "
just_spacing = "space.         "
print(right_space)
print(right_space.rstrip())
print(just_spacing)
print(just_spacing.rstrip())


both_spacing = "     spacing on both sides.      "
print(both_spacing)
print(both_spacing.strip())
