from dataset import Dataset
from sentiment import SentimentAnalyzer
from feature import get_all_basic_features
# from tokenize import DummyTokenizer


def test():
    fn = 'simple-train.txt'
    sentences = Dataset.read_from_file(fn)
    # print DummyTokenizer.tokenize(sentences)

def test2():
    filenames = ['simple-train.txt', 'simple-train-labels.txt',
                 'simple-test.txt', 'simple-test-labels.txt']
    train_sent, train_y, test_sent, test_y = Dataset.read_from_file(*filenames)
    features = get_all_basic_features()
    analyzer = SentimentAnalyzer(features)
    analyzer.train(train_sent, train_y)
    analyzer.predict(test_sent)
    analyzer.score(test_sent, test_y)

if __name__ == '__main__':
    test2()
