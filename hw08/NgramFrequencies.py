class NgramFrequency:

    def __init__(self, text, n):
        self.text = text
        self.n = n
        self.word_counts = {}
        self.total_unigrams = len(text)
    
    def calculate(self):
        unigrams = self.ngrams(self.text.split(), self.n)
        self.total_unigrams = len(unigrams)

        for grams in unigrams:
            self.add_item('_'.join(grams))

        for item in self.top_n_freqs():
            print('    ', item)

    def ngrams(self, words, n):
        ngrams = []
        for i in range(len(words)-n+1):
            ngram = words[i:i+n]
            ngrams.append(ngram)
        return ngrams
    
    def add_item(self, word):
        if word not in self.word_counts:
            self.word_counts[word] = 0
        self.word_counts[word] += 1
    
    def top_n_counts(self):
        return sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    def top_n_freqs(self):
        return list(map(lambda x: (x[0], round(x[1]/self.total_unigrams, 3)), self.top_n_counts()))
    
    def frequency(self, word):
        return self.word_counts[word]