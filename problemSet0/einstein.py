# the goal here is to get an input from the user, this input will mass as integer
# then the program will output the equivalent number of joules as an integer

def main():
    convertion()
    return 0

def convertion():

    print("Conversion started.")
    mass:int = int(input("Gimme some mass brotha!\nMass: "))
    lightSpeed:int = 300000000
    energy:int = mass * (lightSpeed ** 2)
    print(f"Converted mass into energy = {energy}")
    print("Conversion ended")


main()