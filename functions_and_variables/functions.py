# Functions are pieces of code that i can make to use later, there is no limit to
# how many of them i can make. there is no limit to how many of them i can use.
# They can have parameters or not, as shown bellow:

# Functions can have an infinite amount of parameters, but that is not a good
# Practice.
def thisFuncReceivesAParameter(parameter:str):
    print(f"This function received this text as parameter: {parameter}")

def thisFuncNotReceivesAParameter():
    print("This function does not receive a parameter")

# To use a function i need to call it, as shown bellow:

# Calling a function that has parameters
text = "Lakitu"
thisFuncReceivesAParameter(text)

# Calling a function that dont have any parameters
thisFuncNotReceivesAParameter()



