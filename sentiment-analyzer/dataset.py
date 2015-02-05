import codecs


class Dataset(object):


    @staticmethod
    def read_from_db(db, col, q=None):
        pass

    @staticmethod
    def read_from_file(filename):
        #FIXME: Improve
        data = []
        with codecs.open(filename, 'r', 'utf-8') as f:
            for line in f:
                data.append(line.strip())
        return data


