skills: set[str] = {"Python", "Java", "Spring", "Hibernate"}

skills.add("Git")

print(skills)

skills.remove("Java")

print("After remove", skills)

skills.add("Python")
skills.add("Java")

print("After adding again", skills)

forzed_skills: frozenset[str] = frozenset(
    {"Python", "Java", "Spring", "Hibernate", "VSCode"})
print("Frozenset:", forzed_skills)


for skill in forzed_skills:
    print(skill)
