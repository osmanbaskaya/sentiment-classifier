from dataset import Dataset
from sentiment import SentimentAnalyzer
from feature import get_all_features
from tokenize import DummyTokenizer


def test():
    fn = 'simple-dataset.txt'
    sentences = Dataset.read_from_file(fn)
    print DummyTokenizer.tokenize(sentences)

def test2():
    fn = 'simple-dataset.txt'
    sentences = Dataset.read_from_file(fn)
    features = get_all_features()
    analyzer = SentimentAnalyzer(features)

if __name__ == '__main__':
    test2()
