def main():
    number:int = 0
    
    number = int(input("Gimme a number: "))

    is_even(number)

def is_even(number):
    
    if number % 2 == 0:
        print("Is even")
    else:
        print("Its odd")


main()


