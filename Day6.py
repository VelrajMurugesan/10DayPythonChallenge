profile: dict[str, str | int] = {
    "name": "Velraj", "age": 30, "city": "chennai"}

# print(profile['age'])

profile['age'] = 34

# print("updated age : ", profile['age'])


profile['profession'] = "Software Engineer"

# print(profile)

skills: dict[str, str] = {
    "primary": "Python",
    "secondary": "Java",
    "additional": "Spring Boot",
    "versionControl": "Git"
}

# print(skills)

dict_combined: dict[str, str | int] = {**profile, **skills}
# print(dict_combined)


dict_selected: dict[str, str | int] = {
    "name": profile.get("name", ""),
    "age": profile.get("age", 0),
    "primary": skills.get("primary", ""),
    "versionControl": skills.get("versionControl", "")
}

print(dict_selected)
