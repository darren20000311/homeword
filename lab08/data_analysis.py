import re
import csv


class DataAnalysis:

    def __init__(self, file):
        self.data = self.read_data(file)
        self.lang_freqs = {}
        self.tld_freqs = {}

    def read_data(self, file_name):
        with open(file_name) as f:
            reader = csv.reader(f)
            next(reader)
            data = list(reader)
        return data

    def get_lang_freqs(self):
        for row in self.data:
            lang = row[6]
            self.lang_freqs[lang] = self.lang_freqs.get(lang, 0) + 1/1000

    def get_tld_freqs(self):
        for row in self.data:
            email = row[3]
            tld = re.findall(r'\.(\w{2})$', email)
            if tld:
                tld = tld[0]
                self.tld_freqs[tld] = self.tld_freqs.get(tld, 0) + 1/1000

    def top_n_lang_freqs(self, n):
        if not self.lang_freqs:
            self.get_lang_freqs()
        return sorted(self.lang_freqs.items(),
                      key=lambda x: x[1], reverse=True)[:n]

    def top_n_country_tlds_freqs(self, n):
        if not self.tld_freqs:
            self.get_tld_freqs()
        return sorted(self.tld_freqs.items(),
                      key=lambda x: x[1], reverse=True)[:n]
