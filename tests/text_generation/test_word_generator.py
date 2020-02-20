import unittest

from printed_text_dataset.sequence.sequence import Word
from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.word_generator import WordGenerator

class TestWordGenerator(unittest.TestCase):
    def test_sample(self):
        """Check if the return type of the function is Word
        Check if each character of the sampled word is in the unicode distribution
        Check if the length of the sampled word is in the length distribution
        """

        unicode_distribution = Distribution(dict(zip(list("abcde"), [0.1, 0.2, 0.3, 0.1, 0.3])))
        length_distribution = Distribution(dict(zip(range(1,6), [0.3, 0.35, 0.1, 0.2, 0.05])))
        wg = WordGenerator(unicode_distribution, length_distribution)
        nb_iter = 2000

        for _ in range(nb_iter):
            sample = wg.sample()
            self.assertTrue(isinstance(sample, Word))
            self.assertTrue(len(sample) in wg.length_distribution.prob_dict.keys())
            for c in sample:
                self.assertTrue(c in unicode_distribution.prob_dict.keys())
