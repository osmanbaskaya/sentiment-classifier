import codecs


class Dataset(object):


    @staticmethod
    def read_from_db(db, col, q=None):
        pass

    @staticmethod
    def read_from_file(*filenames):
        #FIXME: Improve
        all = []
        for fn in filenames:
            data = []
            with codecs.open(fn, 'r', 'utf-8') as f:
                for line in f:
                    data.append(line.strip())
            all.append(data)
        return all



