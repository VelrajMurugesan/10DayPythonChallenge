a = 1
b = 1.1
c = 'velraj'
d = True
e = None
f: list[object] = [1, 2.2, True, 'Velraj']
g = (3, 4.4, 'world', True)
h: dict[str, str | int | bool] = {
    'name': 'velraj', 'age': 25, 'is_student': False}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

# String
str1 = "Hello \"World\"!"

print(str1)

# message body using multiline string
message = """Hello User,
Welcome to the Python programming world.    
Have a great day!
"""

print(message)
