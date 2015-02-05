
class DummyTokenizer(object):

    @staticmethod
    def tokenize(sentences):
        return map(unicode.split, sentences)
