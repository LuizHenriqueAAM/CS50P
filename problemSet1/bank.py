greeting = input("Greeting: ")

if greeting.startswith("hello") == True:
    print("$0")
elif greeting.startswith("h") == True and greeting.find("hello") == -1:
    print("$20")
else:
    print("$100")
