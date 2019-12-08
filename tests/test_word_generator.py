import unittest
from printed_text_dataset.word_generator import WordGenerator

class TestWordGenerator(unittest.TestCase):
    def test_sample(self):
        """Chack if the characters generated belongs to unicode_characters
        Check length_distribution probabilistic property"""
        eps = 0.01
        wg = WordGenerator(list("abcde"), [0.3, 0.35, 0.1, 0.2, 0.05])
        nb_iter = 50000
        counter = [0,] * len(wg.length_distribution)
        for _ in range(nb_iter):
            word = wg.sample()
            for c in word:
                self.assertIn(c, wg.unicode_characters)
            counter[len(word)-1] += 1

        counter = [i/nb_iter for i in counter]
        for i in range(len(counter)):
            self.assertAlmostEqual(counter[i], wg.length_distribution[i], delta=eps)

