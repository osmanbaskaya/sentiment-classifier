from abc import abstractmethod
from itertools import combinations_with_replacement
from sklearn.feature_extraction.text import CountVectorizer


__all__ = ['WordCountFeature',
           'CharacterCountFeature',
           'UpperCaseCountFeature',
           'PunctuationSequenceFeature']


def get_all_basic_features():
    return filter(lambda cls: cls.get_feature_type() == 'basic',
                  map(lambda cls: globals()[cls], __all__))


class Feature(object):
    pass


class BasicFeature(Feature):
    """
    Basic Feature is a feature that doesn't need to transform training data to
    transform test data. That is, the same method body can be used for training
    and test datasets.
    """

    def __new__(cls, *args, **kwargs):
        raise ValueError("Not allowed to create instance. Use static methods "
                         "instead")

    @classmethod
    @abstractmethod
    def fit_transform(cls, sentences):
        raise NotImplementedError("Implement me")

    @classmethod
    def transform(cls, sentences):
        return cls.fit_transform(sentences)

    @staticmethod
    def get_feature_type():
        return "basic"


class ComplexFeatures(Feature):

    @abstractmethod
    def fit_transform(self, sentences):
        raise NotImplementedError("Implement me")

    @abstractmethod
    def transform(self, sentences):
        raise NotImplementedError("Implement me")

    @staticmethod
    def get_feature_type():
        return "complex"

class WordCountFeature(BasicFeature):


    @classmethod
    def transform_one(cls, tokens):
        """
        >>> tokens = ["Love", "me", "two", "times", ",", "baby"]
        >>> WordCountFeature.transform_one(tokens)
        6
        """
        return len(tokens)

    @classmethod
    def fit_transform(cls, sentences):
        return map(len, sentences)


class CharacterCountFeature(BasicFeature):

    @classmethod
    def fit_transform(cls, sentences):
        return map(lambda sentence: sum(map(len, sentence)), sentences)


class UpperCaseCountFeature(BasicFeature):
    """
    >>> sentences = [['Hello', "HELLO", 'HeLlO', 'elloh'], ['HELLO', 'HELLO']]
    >>> UpperCaseCountFeature.fit_transform(sentences)
    [1, 2]
    """
    @classmethod
    def fit_transform(cls, sentences):
        return map(lambda sentence: sum(map(lambda x: x.isupper(),
                                            sentence)), sentences)


class PunctuationSequenceFeature(ComplexFeatures):

    def __init__(self, ngram_range=(2, 2), punc_vocab='!,.?'):
        self.vectorizer = None
        self.ngram_range = ngram_range
        self.punc_vocab = punc_vocab
        self.vocabulary = PunctuationSequenceFeature.create_vocab(punc_vocab,
                                                                  ngram_range)

    @staticmethod
    def create_vocab(punc_vocab, ngram_range):
        # FIXME Doesn't create all combinations
        vocab = []
        min_ngram, max_ngram = ngram_range
        for val in xrange(min_ngram, max_ngram+1):
            vocab.extend([' '.join(t) for t in
                          combinations_with_replacement(punc_vocab, val)])
        return vocab

    def transform(self, sentences):
        pass

    def fit_transform(self, sentences):
        self.vectorizer = CountVectorizer(tokenizer=lambda x: x,
                                          lowercase=False,
                                          vocabulary=self.vocabulary,
                                          ngram_range=self.ngram_range,
                                          min_df=0)
        
