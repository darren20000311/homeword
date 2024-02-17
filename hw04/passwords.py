import random
print("Welcome to the username and password generator!")
FIRST_NAME = input("Please input your first name: ")
LAST_NAME = input("Please input your last name: ")
FAVORITE_WORD = input("Please input your favorite word:")
def user_name():
    if len(LAST_NAME) < 7:
        #Since if the length of first name is less than 7, I need to add * until its length become 7
        LAST_NAME = LAST_NAME + '*' * (7-len(LAST_NAME))
    #The user name's first letter needs to be the first name's first letter, so I pick the first index of FIRST_NAME
    USER_NAME_WORD = FIRST_NAME[0] + LAST_NAME
    #Since I also need to have 2 random numbers at the end of user name, I use the below way to pick 2 random numbers add to my user name
    USER_NAME_NUMBER = str(random.randint(0,99))
    print("Thanks", FIRST_NAME, "your user name is "+ USER_NAME_WORD.lower()+ USER_NAME_NUMBER)
user_name()

def pass_words():
    #I follow the instruction that transfer the original letters to the similar letter to symbols or numbers
    for word in FIRST_NAME and LAST_NAME:
        if 'a' in FIRST_NAME and LAST_NAME:
            word = word.replace('a', '@')
        elif 'l' in FIRST_NAME and LAST_NAME:
            word = word.replace('l', '1')
        elif 'o' in FIRST_NAME and LAST_NAME:
            word = word.replace('o', '0')
        elif 's' in FIRST_NAME and LAST_NAME:
            word = word.replace('s', '$')
    #The instruction says the password needs to be lower case, so I use .lower() to make it right.
    PASS_WORD_01 = FIRST_NAME.lower()+str(random.randint(0,99))+LAST_NAME.lower()
    print("password1: "+PASS_WORD_01.replace('*', ''))
    #The instruction says I need to pick the first letter of my first name,last name, my favorite word, and the last letter of my first name, last name, my favorite word.
    #And I just use the lower() and upper() to do this.
    PASS_WORD_02 = FIRST_NAME[0].lower()+FIRST_NAME[-1].upper()+LAST_NAME[0].lower() + LAST_NAME[-3].upper() + FAVORITE_WORD[0].lower() + FAVORITE_WORD[-1].upper()
    print("password2: " + PASS_WORD_02)
    #Since the instruction says I can get a random-length portion of the first name, combined with random-length portions of the favorite word and last name in any order,
    #I use the sorted method, so that I can get the orderd letters form the word I enter.
    #And random.choice method can give me any numbers of the word that I enter
    PASS_WORD_003 = sorted(random.choice(FIRST_NAME)) + sorted(random.choice(LAST_NAME[:4])) + sorted(random.choice(FAVORITE_WORD))
    PASS_WORD_03 = ''.join(PASS_WORD_003)
    print("password3: " + PASS_WORD_03)
pass_words()