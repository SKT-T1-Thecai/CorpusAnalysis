from line import Line
from all_tokenizers import tokenizers
import numpy as np
from visualize import draw_distribution
from pyecharts.charts import Page

class Corpus:
    '''
    Abstract corpus, which could be single corpus, bilingual corpus or corpora.
    '''
    def __init__(self, path):
        return NotImplementedError

    def build_vocabs(self):
        return NotImplementedError

    def analyse(self):
        return NotImplementedError

class SingleCorpus(Corpus):
    '''
    Corpus which is built from a single file or several fusible corpora.
    '''
    def __init__(self, path,tokenizer=None):
        if tokenizer is not None:
            assert isinstance(tokenizer,str)
            assert list(tokenizers.keys()).__contains__(tokenizer)
        lines = open(path,"r",encoding="utf-8").readlines()
        self.lines = [Line(l,tokenizer) for l in lines]
        # self.char_vocab = self.build_char_vocab()
        self.build_word_vocab()

    def build_char_vocab(self):
        return NotImplementedError

    def build_word_vocab(self):
        dictionary = {}
        for line in self.lines:
            assert line.tokenized
            for word in line.tokenized_list:
                if word in dictionary:
                    dictionary[word] +=1
                else:
                    dictionary[word] =1
        dictionary = list(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        self.word_vocab = dictionary


    def analyse(self):
        print("########单一语料库分析########")
        print("行总数：{}".format(len(self.lines)))
        print("句子总数：{}".format(np.sum(np.array([line.sentence_num for line in self.lines]))))
        print("字符总数：{}".format(np.sum(np.array([line.character_num for line in self.lines]))))
        print("单词总数：{}".format(np.sum(np.array([line.nums_words for line in self.lines]))))
        # print("字符总种类数：{}".format())
        print("单词总种类数：{}".format(len(self.word_vocab)))
        print("平均长度（字符）：{}".format(np.mean(np.array([line.len for line in self.lines]))))
        print("平均长度（单词）：{}".format(np.mean(np.array([line.nums_words for line in self.lines]))))
        print("语料库词表：")
        print(self.word_vocab)
        
        page = Page()
        page.add(draw_distribution([line.len for line in self.lines],"长度（字符）分布表"))
        page.add(draw_distribution([line.nums_words for line in self.lines],"长度（词）分布表"))
        page.render("single_corpus.html")

        
        


