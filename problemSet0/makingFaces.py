def main():
    text = input("Write something and put a :) or a :( on it: ")
    convert(text)

def convert(text:str):
    newText:str
    newText = text.replace(":)", "🙂")
    newText = newText.replace(":(", "🙁")
    print(f"{newText}")


main()