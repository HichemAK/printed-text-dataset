from unittest import TestCase

from printed_text_dataset.sequence.sequence import Sentence, Separator
from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.sentence_generator import SentenceGenerator
from printed_text_dataset.text_generation.text_generator import TextGenerator
from printed_text_dataset.text_generation.word_generator import WordGenerator


class TestTextGenerator(TestCase):
    def test_sample(self):
        """Check that Text is composed of only (Sentence, Separator)
        Check that Sentence has at least (n) characters ; n = min(k for k in min_length_distribution._keys)
        """
        unicode_distribution = Distribution(dict(zip(["a", "b", "c"], [1, ] * 3)))
        length_distribution = Distribution(dict(zip(range(1, 5), [1, ] * 5)))
        wg = WordGenerator(unicode_distribution=unicode_distribution, length_distribution=length_distribution)

        min_length_distribution = Distribution(dict(zip(range(10, 31, 10), [1, ] * 3)))
        punctuation_prob = 0.1
        punctuation_sign_distribution = Distribution(dict(zip([",", "."], [0.7, 0.3])))
        punctuation_format_distribution = Distribution(dict(zip(["ps", ], [1, ])))

        sg = SentenceGenerator(word_generator=wg, min_length_distribution=min_length_distribution,
                               punctuation_prob=punctuation_prob,
                               punctuation_sign_distribution=punctuation_sign_distribution, separator=" ",
                               punctuation_format_distribution=punctuation_format_distribution)

        tmin_length_distribution = Distribution(dict(zip(range(30, 501, 10), [1, ] * 48)))
        separator_prob = 0.2

        tg = TextGenerator(sentence_generator=sg, min_length_distribution=tmin_length_distribution,
                           separator_prob=separator_prob, separator='\n')

        min_length = min(k for k in tmin_length_distribution._keys)
        nb_iter = 2000
        for _ in range(nb_iter):
            text = tg.sample()
            self.assertTrue(text.length >= min_length)
            for c in text:
                self.assertTrue(isinstance(c, (Sentence, Separator)))
