import unittest
from printed_text_dataset.text_gen.word_generator import WordGenerator

class TestWordGenerator(unittest.TestCase):
    def test_WordGenerator(self):
        """Check that if character_distribution is not provided the apparition of each character is equiprobable"""
        wg = WordGenerator(list("abcde"), [0.3, 0.35, 0.1, 0.2, 0.05])

        self.assertEqual(len(wg.unicode_characters), len(wg.character_distribution))
        for i in range(1, len(wg.character_distribution)-1):
            self.assertEqual(wg.character_distribution[i], wg.character_distribution[0])

    def test_sample(self):
        """Chack if the characters generated belongs to unicode_characters
        Check length_distribution probabilistic property
        Check character_distribution probabilistic property
        """

        eps = 0.01
        wg = WordGenerator(list("abcde"), [0.3, 0.35, 0.1, 0.2, 0.05], character_distrbution=[0.1, 0.2, 0.3, 0.1, 0.3])
        nb_iter = 50000

        nb_chars = 0
        counter_length = [0,] * len(wg.length_distribution)

        counter_chars = [0,] * len(wg.unicode_characters)

        for _ in range(nb_iter):
            word = wg.sample()
            nb_chars += len(word)
            for c in word:
                counter_chars[wg.unicode_characters.index(c)] += 1
                self.assertIn(c, wg.unicode_characters)
            counter_length[len(word)-1] += 1

        counter_chars = [i / nb_chars for i in counter_chars]
        counter_length = [i/nb_iter for i in counter_length]

        # Check length distribution
        for i in range(len(counter_length)):
            self.assertAlmostEqual(counter_length[i], wg.length_distribution[i], delta=eps)

        # Check character distribution
        for i in range(len(counter_chars)):
            self.assertAlmostEqual(counter_chars[i], wg.character_distribution[i], delta=eps)

