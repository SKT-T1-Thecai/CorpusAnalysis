from all_tokenizers import tokenizers
from errors import TokenizerNotInListError
from nltk.tokenize import sent_tokenize
class Line:
    def __init__(self,full_string,tokenizer=None):
        self.origin_string = full_string
        self.tokenized = False
        if tokenizer is not None:
            self.tokenized = True
            self.tokenized_list = tokenizers[tokenizer](self.origin_string)
            self.tokenized_string = " ".join(self.tokenized_list)

    @property
    def len(self):
        return len(self.origin_string)

    @property
    def nums_words(self):
        if self.tokenized:
            return len(self.tokenized_list)
        else:
            return len(self.origin_string.split(" "))
    
    @property
    def sentence_num(self):
        return len(sent_tokenize(self.origin_string))
    @property
    def character_num(self):
        return self.origin_string.replace(" ","").replace("\n","").__len__()




        