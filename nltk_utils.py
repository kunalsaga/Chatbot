from os import name
import nltk

import numpy as np

# nltk.download('punkt')

from nltk.stem.porter import PorterStemmer
from pip import main
from torch import dtype

Stemmer = PorterStemmer()


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return Stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag


# sentence = ["hello", "how", "are", "you"]
# words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
# bog = bag_of_words(sentence, words)
# print(bog)


# if __name__ == "__main__":
#     a="Hello, thanks for visiting"
#     print(a)
#     a=tokenize(a)
#     print(a)
#     words = ["organize", "organizes", "organizing"]
#     stemmedwords = [stem(w) for w in words]
#     print(stemmedwords)
