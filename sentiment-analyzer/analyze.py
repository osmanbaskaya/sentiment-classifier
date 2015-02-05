__author__ = 'thorn'

import pipeline
from dataset import Dataset
from tokenize import DummyTokenizer



def test():
    fn = 'simple-dataset.txt'
    sentences = Dataset.read_from_file(fn)
    print DummyTokenizer.tokenize(sentences)


if __name__ == '__main__':
    test()
