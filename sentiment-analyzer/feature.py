from abc import abstractmethod


class Feature(object):

    @staticmethod
    @abstractmethod
    def transform(sentences):
        raise NotImplementedError("Implement me")


class WordCountFeature(Feature):

    def __new__(cls, *args, **kwargs):
        raise ValueError("Not allowed to create instance. Use staticmethod")

    @staticmethod
    def transform_one(tokens):
        """
        >>> tokens = ["Love", "me", "two", "times", ",", "baby"]
        >>> WordCountFeature.transform_one(tokens)
        6
        """
        return len(tokens)

    @staticmethod
    def transform(sentences):
        return map(len, sentences)







