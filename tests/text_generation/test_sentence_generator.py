import unittest

from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.sentence_generator import SentenceGenerator
from printed_text_dataset.text_generation.word_generator import WordGenerator
from printed_text_dataset.sequence.sequence import Word, Separator, Punctuation

class TestSentenceGenerator(unittest.TestCase):
    def test_sample(self):
        """Check that Sentence is composed of only (Word, Separator, Punctuation)
        Check that Sentence has at least (n) characters ; n = min(k for k in min_length_distribution._keys)
        """
        unicode_distribution = Distribution(dict(zip(["a","b","c"], [1,]*3)))
        length_distribution = Distribution(dict(zip(range(1,5), [1,] * 5)))
        wg = WordGenerator(unicode_distribution=unicode_distribution, length_distribution=length_distribution)

        min_length_distribution = Distribution(dict(zip(range(10,51,10), [1,] * 5)))
        punctuation_prob = 0.1
        punctuation_sign_distribution = Distribution(dict(zip([",","."],[0.7,0.3])))
        punctuation_format_distribution = Distribution(dict(zip(["ps",], [1,])))
        separator = " "

        sg = SentenceGenerator(word_generator=wg, min_length_distribution=min_length_distribution,
                               punctuation_prob=punctuation_prob,
                               punctuation_sign_distribution=punctuation_sign_distribution,separator=separator,
                               punctuation_format_distribution=punctuation_format_distribution)

        nb_iter = 2000
        min_length = min(k for k in min_length_distribution._keys)
        for _ in range(nb_iter):
            sentence = sg.sample()
            self.assertTrue(len(str(sentence)) >= min_length)
            for c in sentence:
                self.assertTrue(isinstance(c, (Word, Separator, Punctuation)))



