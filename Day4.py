for i in range(0, 5):
    print("Hello World " + str(i))

person: dict[str, int | str] = {
    'name': 'Velraj', 'age': 34, 'city': 'Chennai'}

country: dict[str, str] = {
    'name': 'India', 'capital': 'New Delhi', 'currency': 'INR'}


for key in person:
    print(f"{key}: {person[key]}")

for text in country.values():
    print(text)

# converting 2 list into dictionary

name: list[str] = ['Velraj', 'Murugesan', 'Kumar']
age: list[int] = [25, 30, 35]
person_dict: dict[str, int] = dict(zip(name, age))
print(person_dict)
