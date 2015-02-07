import sys
import logging
from itertools import izip
from tag import ArkTwitterTagger, DummyTokenizer
from sklearn.svm import *
from sklearn.metrics import accuracy_score


handler = logging.StreamHandler(sys.stdout)
LOGGER = logging.getLogger()
LOGGER.addHandler(handler)
LOGGER.setLevel(logging.DEBUG)


class SentimentAnalyzer(object):

    def __init__(self, features, tokenizer=None, tagger=None, optimize=False):
        self.features = features
        self.tokenizer = tokenizer
        self.tagger = tagger
        self.optimize = optimize
        self.classifier = LinearSVC(verbose=True)

        if tokenizer is None:
            self.tokenizer = DummyTokenizer
        if tagger is None:
            self.tagger = ArkTwitterTagger

        self.transformed_data = []

    def preprocess(self, sentences, config=None):
        #TODO: pos tagging / tokenizing
        if config is None:
            self.tagger = self.tagger()
        # tokenized = self.tokenizer.tokenize(sentences)
        tagged = self.tagger.tokenize_and_tag(sentences, no_confidence=True)
        for result in tagged:
            yield result[:2]


    def train(self, training_data, training_labels):

        X = training_data
        y = training_labels

        assert len(X) == len(y), "Missing data. # of Labels != # of sentences"

        if len(self.transformed_data) != 0:
            LOGGER.warning("fit_transform is already done. Removing leftover "
                           "data")
            self.transformed_data = []

        X = self.preprocess(training_data)

        for feature in self.features:
            self.transformed_data.append(feature.fit_transform(X))

        #FIXME: matlabish matrix concatenation needed
        X = []
        for row in izip(*self.transformed_data):
            X.append(row)

        self.classifier.fit(X, y)
        LOGGER.debug('Classifier is trained. %s' % self.classifier)

    def optimize(self):
        pass

    def predict(self, test_data):
        assert len(self.transformed_data) != 0, "Train the model first."

        X = self.preprocess(test_data)
        transformed = []
        for feature in self.features:
            transformed.append(feature.transform(X))

        X = []
        for row in izip(*transformed):
            X.append(row)

        return self.classifier.predict(X)

    def score(self, test_data, test_labels, score_func=None):

        X = test_data
        y = test_labels

        if score_func == None:
            score_func = accuracy_score

        predictions = self.predict(X)
        score = score_func(predictions, y)
        LOGGER.info("Score: %.4f" % score)
        return score, predictions



