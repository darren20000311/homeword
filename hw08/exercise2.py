from NgramFrequencies import *
from text_cleaner import *

def main():
    cleaned_text = {}
    with open('corpse_bride.txt', 'r') as f:
        nf = f.read()
        clean= TextCleaner(nf)
        cleaned_text = clean.clean_text()
        print("Top 10 unigrams:")
        ngram = NgramFrequency(cleaned_text, 1)
        ngram.calculate()
        print("Top 10 bigrams:")
        ngram = NgramFrequency(cleaned_text, 2)
        ngram.calculate()
        print("Top 10 trigrams:")
        ngram = NgramFrequency(cleaned_text, 3)
        ngram.calculate()

    
        
        
main()