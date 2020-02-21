import random

from printed_text_dataset.sequence.sequence import Text, Separator
from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.generator import _Generator
from printed_text_dataset.text_generation.sentence_generator import SentenceGenerator


class TextGenerator(_Generator):
    """A class that generates texts through calling the function sample() which returns an instance of the class
        Text"""
    def __init__(self, sentence_generator : SentenceGenerator, min_length_distribution : Distribution, separator_prob,
                 separator='\n'):
        """

        :param sentence_generator: Instance of class SentenceGenerator that is used to generate sentences
        :param min_length_distribution: The distribution of the minimum length of the text (in number of characters)
        :param separator_prob: It's the probability of the presence of a separator between two consecutive sentences
        :param separator: String that separates 2 sentences. Default = '\n'
        """
        super().__init__()
        self.sentence_generator = sentence_generator
        self.min_length_distribution = min_length_distribution
        self.separator_prob = separator_prob
        self.separator = separator

    def sample(self):
        """Generates a text. Returns a Text object
        The function chooses a minimun length (l) for the sentence according to min_length_distribution.
        While the length of the text < min_length:
            We generate a sentence and add it to the text. Before we generate the next sentence, we put a separator with
            a probability equal to 'self.separator_prob'.
        """
        min_length = self.min_length_distribution.sample()
        text = Text()
        while len(text) < min_length:
            sentence = self.sentence_generator.sample()
            text.append(sentence)

            put_separator = self._get_put_separator()
            if put_separator:
                text.append(Separator([self.separator, ]))

    def _get_put_separator(self):
        """returns (x) that takes values (False, True) so that P(x=True) = self.punctuation_prob and
        P(x=False) = 1 - self.punctuation_prob (Bernoulli Distribution)"""
        return random.random() < self.punctuation_prob
