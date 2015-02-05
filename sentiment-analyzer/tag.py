# -*- coding: utf-8 -*-
import os
from subprocess import Popen, PIPE


class ArkTwitterTagger(object):
    """
    CMU Ark's Tokenizer and Tagger: http://www.ark.cs.cmu.edu/TweetNLP/
    """

    def __init__(self, lib_directory=None):
        if lib_directory is None:
            lib_directory = "/Users/thorn/playground/ark-tweet-nlp-0.3.2"
        self.lib_directory = lib_directory
        self.command = os.path.join(lib_directory, "runTagger.sh")

    def tokenize_and_tag(self, sentences, no_confidence=False):
        command = [self.command]
        if no_confidence:
            command.append('--no-confidence')

        tagged = ArkTwitterTagger._run_command(command, sentences)
        return map(lambda s: s.split('\t'), tagged)

    def tokenize(self, sentences):
        command = [self.command, '--just-tokenize']
        tokenized_sentences = ArkTwitterTagger._run_command(command, sentences)
        return map(lambda s: s.split('\t')[0], tokenized_sentences)

    @staticmethod
    def _run_command(command, sentences):
        p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, _ = p.communicate('\n'.join(sentences).encode('utf-8'))
        return stdout.split('\n')[:-1]


def test():
    tagger = ArkTwitterTagger()
    sentences = ["Hello how are you", 'Rakı is a good']
    print tagger.tokenize_and_tag(sentences)
    # print tagger.tokenize(sentences)


if __name__ == '__main__':
    test()