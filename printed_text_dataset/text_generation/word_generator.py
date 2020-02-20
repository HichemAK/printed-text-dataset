from printed_text_dataset.sequence.sequence import Word
from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.generator import _Generator


class WordGenerator(_Generator):
    """A class that generates words through calling the function sample()"""
    def __init__(self, unicode_distribution : Distribution, length_distribution : Distribution):
        """unicode_characters : The list of characters that will be used to generate the words

        length_distribution : A list of integers that represents the probability of each length to be chosen during
        sampling. Example : [0.7, 0.1, 0.2] means the word has a length of 1 with a probability of 0.7

        character_distribution : A list of integers that represents the probability of each character to be chosen
        during sampling
        """
        super().__init__()
        self.unicode_distribution = unicode_distribution
        self.length_distribution = length_distribution

    def sample(self):
        """Generates a random word and return a list that contains its characters"""
        word = [self.unicode_distribution.sample() for _ in range(self.length_distribution.sample())]
        return Word(word)

