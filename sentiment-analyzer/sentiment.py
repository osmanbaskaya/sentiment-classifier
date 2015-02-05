from tag import ArkTwitterTagger
from tokenize import DummyTokenizer
from sklearn.svm import LinearSVC


class SentimentAnalyzer(object):

    def __init__(self, features, tokenizer=None, tagger=None, optimize=False):
        self.features = features
        self.tokenizer = tokenizer
        self.tagger = tagger
        self.optimize = optimize
        self.classifier = LinearSVC()

        if tokenizer is None:
            self.tokenizer = DummyTokenizer
        if tagger is None:
            self.tagger = ArkTwitterTagger

    def fit_transform(self, training_data):
        pass

    def optimize(self):
        pass

    def transform(self, test_data):
        pass

    def predict(self, test_data):
        pass

    def score(self, test_data):
        pass

