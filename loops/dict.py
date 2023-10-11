#   dist is like a object in js

# students = {"Hero": "Hey", "Harry": "Hey", "Ron": "Hey", "Draco": "Hey"}

# print(students["Hero"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# for student in students:
#     print(student, students[student], sep=", ")


students = [
    {
        "name": "Hero",
        "house": "Hey",
        "pat": "otter",
    },
    {
        "name": "Harry",
        "house": "Hey",
        "pat": "Stag",
    },
    {
        "name": "Ron",
        "house": "Hey",
        "pat": "jack",
    },
    {"name": "Draco", "house": "Hey", "pat": None},
]

# None is the keyword

for student in students:
    print(student["name"], student["house"], student["pat"], sep=", ")
