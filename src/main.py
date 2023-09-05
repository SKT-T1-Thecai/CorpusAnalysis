# 需求分析

# 单一语料库
## 数字：行总数，句子总数，字符总数，单词总数，字符总种类数，单词总种类数，非重复句子占比，最大/小字符数， 
## 数字（续）：最大/小单词数 最大/小长度
## 均值方差： 句行比 字符行比 单词行比 
## 分布：单词分布，字符分布，行长度分布， 行语言分布（fasttext）
## 最多的前N个字符，最多的前N个单词， 重复最多的N句话

# 双语语料库
## 各自的单一语料库分析
## 数字 非重复句对占比 
## 分布 长度比分布

# 语料库集
import argparse
from corpus import SingleCorpus
from visualize import draw_distribution

if __name__ == "__main__":
    sc = SingleCorpus("D:/CorpusAnalysis/data/jianwei.zh.txt","zh_jieba")
    sc.analyse()
