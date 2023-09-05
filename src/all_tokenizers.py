import jieba
import nltk

def zh_jieba(string):
    return list(jieba.cut(string))

def en_nltk(string):
    return nltk.word_tokenize(string)

tokenizers = {
    "zh_jieba": zh_jieba,
    "en_nltk": en_nltk
}
