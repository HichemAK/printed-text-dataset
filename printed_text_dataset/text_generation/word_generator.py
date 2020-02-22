from printed_text_dataset.sequence.sequence import Word
from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.generator import _Generator


class WordGenerator(_Generator):
    """A class that generates words through calling the function sample()"""
    def __init__(self, unicode_distribution : Distribution, length_distribution : Distribution):
        """unicode_distribution : The distribution of the unicode characters that compose the word

        length_distribution : The distribution of the length of the word
        """
        super().__init__()
        self.unicode_distribution = unicode_distribution
        self.length_distribution = length_distribution

    def sample(self):
        """Generates a random word and return an instance of class Word.
        The function chooses the length (l) of the word according to length_distribution and generates the (l)
        characters that compose the sampled word according to unicode_distribution"""
        word = [self.unicode_distribution.sample() for _ in range(self.length_distribution.sample())]
        return Word(word)

