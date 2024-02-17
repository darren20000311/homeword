import re

def main():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()
        #use split to split the whole content into words, and count them up.
        word_count = len(text.split())
        #count the whole single characters in the content
        char_count = len(text)
        #Because we only want to count the letters and numbers, I use
        #re.findall method, 
        # and then select only the range of lower letter and upper letter and numbers
        alphanumeric_count = len(re.findall(r'[a-zA-Z0-9]', text))

        print(f'Words: {word_count}')
        print(f'Characters: {char_count}')
        print(f'Letters & numbers: {alphanumeric_count}')

    except FileNotFoundError:
        print(f"Can't open {file_name}")


main()
