name:str

name = input("What's your name? ")

if name == "harry" or "Harry" or "hermione" or "Hermione" or "ron" or "Ron":
    print("Gryffindor")

elif name == "draco" or "Draco":
    print("Slytherin")

else:
    print("Who")
name = (45, 78)
match name:
    case "harry":
        print("Gryffindor")
    case "hermione":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who?")
