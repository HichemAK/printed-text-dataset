import unittest
from printed_text_dataset.text_generation.sentence_generator import SentenceGenerator
from printed_text_dataset.text_generation.word_generator import WordGenerator

class TestSentenceGenerator(unittest.TestCase):
    def setUp(self):
        self.wg = WordGenerator(unicode_characters=list("abc"), length_distribution=[0.7, 0.4])
        self.sg = SentenceGenerator(word_generator=self.wg, length_distribution=list(range(20, 0, -1)),
                               punctuation_signs=[',', '.'], punctuation_prob=0.1,
                               punctuation_sign_distribution=[0.6, 0.4], separator=' ',
                               punctuation_format=["sp", "ps"],
                               punctuation_format_distribution=[0.3, 0.7])
        self.eps = 0.01

    def test_sample(self):
        """Check that sentence have at least 1 character
        Check that there isn't two consecutive punctuation signs
        Check that there isn't two consecutive separators
        """
        eps = 0.01


        nb_iter = 10000
        for _ in range(nb_iter):
            sentence = self.sg.sample()
            # Check sentence not empty
            self.assertTrue(len(sentence) > 0)

            for i in range(len(sentence)-1):
                if ("".join(sentence[i]).strip(self.sg.separator) in self.sg.punctuation_signs) and \
                        ("".join(sentence[i+1]).strip(self.sg.separator) in self.sg.punctuation_signs):
                    self.fail("There is two consecutive punctuations")

                if len(sentence[i]) == 1 and sentence[i] == " " and len(sentence[i+1]) == 1 and sentence[i+1] == " ":
                    self.fail("There is two consecutive separators")



