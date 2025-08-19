def main():
    text = input("Write something and put a :) or a :( on it")
    convert(text)

def convert(text:str):
    text.replace(":)", "🙂")
    text.replace(":(", "🙁")
    print(f"{text}")


main()