""" # String
str1 = "Hello \"World\"!"

print(str1)

# message body using multiline string
message = ""\"Hello User,
Welcome to the Python programming world.
Have a great day!
""\"

print(message)

# Expression
#
fName = "Velraj"
lName = "Murugesan"
fullname_old = fName + " " + lName
print(fullname_old)
# any expression can be used inside {} like 2 + 2, len(fName) and so on...
fullName = f"{fName} {lName}"
print(fullName) """


# useful string methods
sample_str = "  Hello World! Welcome to Python Programming.  "
print(sample_str.casefold)
