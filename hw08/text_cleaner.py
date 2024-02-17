import re

class TextCleaner:
    def __init__(self, text):
        self.text = text
    
    def clean_text(self):
        text = self.text.lower()
        text = text.replace(",", " COMMA").replace("mr.", "mr").replace("dr.", "dr")
        text = re.sub(r'[^\w,\s\']', '', text)
        return text