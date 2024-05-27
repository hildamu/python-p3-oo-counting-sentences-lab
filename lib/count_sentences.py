#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self.value = value
        print("The value must be a string.")
            
        self.value = value

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        
        if not self.value:
            return 0
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)
