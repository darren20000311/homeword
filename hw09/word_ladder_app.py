from word_ladder import WordLadder


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    english_words = load_words()

    while True:
        w1, w2 = input("> ").split()
        # Create a WordLadder object
        wl = WordLadder(w1, w2, english_words[len(w1)])
        # Generate the word ladder
        word_ladder = wl.make_ladder()
        print("Ladder: ", word_ladder)


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words

main()

# The output will be as follow:
# darren@xiezhixingdeMacBook-Pro hw09 % /usr/local/bin/python3 /Users/darren/Desktop/CS5001/hw09/word_ladder_app.py
# > cat hat
# Ladder:  cat    hat
# > love hate
# Ladder:  love   hove    have    hate
# > angel devil
# Ladder:  angel  anger   aeger   leger   lever   level   devel   devil
# > earth ocean
# Ladder:  earth  barth   barih   baris   batis   bitis   aitis   antis   antas   antal   ontal   octal   octan   ocean
