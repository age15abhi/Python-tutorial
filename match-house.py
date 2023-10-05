name = input("what is your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Glyffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who")


# Here is the use of match keyword in the python
#  it is same as the switch case statement in the javascript
# the name is only different but the working is same in the both
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
