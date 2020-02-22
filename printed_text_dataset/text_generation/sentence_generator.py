import random

from printed_text_dataset.sequence.sequence import Sentence, Separator, Punctuation
from printed_text_dataset.text_generation.distribution import Distribution
from printed_text_dataset.text_generation.generator import _Generator
from printed_text_dataset.text_generation.word_generator import WordGenerator

class SentenceGenerator(_Generator):
    """A class that generates sentences through calling the function sample() which returns an instance of the class
    Sentence"""
    def __init__(self, word_generator : WordGenerator, min_length_distribution : Distribution, punctuation_prob,
                 punctuation_sign_distribution : Distribution, separator=" ",
                 punctuation_format_distribution : Distribution = None):
        """word_generator : an instance of the class word_generator.WordGenerator that is used to generate words

        min_length_distribution : The distribution of the minimum length of the sentence (in number of characters)

        punctuation_prob : It's the probability of the presence of a punctuation sign between two consecutive words

        punctuation_sign_distribution : The distribution of punctuation signs

        separator : A String of characters that separates two consecutive words in the sentence. default = ' '

        punctuation_format : The format used to write punctuation default : ['sps', 'ps', 'sp']. 'sps' means that when
        we put punctuation we want to put first a separator (s) then the sign of punctuation (p) then another separator
        (s)

        punctuation_format_distribution : The distribution of punctuation formats. By default =
        Distribution({'sps' : 1/3, 'ps' : 1/3, 'sp' : 1/3]). 'sps' means that when we put punctuation we want to put
        first a separator (s) then the sign of punctuation (p) then another separator (s)
        """
        super().__init__()
        self.word_generator = word_generator
        self.min_length_distribution = min_length_distribution
        self.separator = separator
        self.punctuation_prob = punctuation_prob
        self.punctuation_sign_distribution = punctuation_sign_distribution
        if punctuation_format_distribution is None:
            self.punctuation_format_distribution = Distribution(dict(zip(["sps", "ps", "sp"], [1/3,] * 3)))
        else:
            self.punctuation_format_distribution = punctuation_format_distribution

    def sample(self):
        """Generates a sentence. Returns a Sentence object
        The function chooses a minimum length (l) for the sentence according to min_length_distribution.
        While the length of the sentence < min_length:
            We generate a word and add it to the sentence. Before we generate
            the next word, we put a separator or a punctuation sign according to punctuation_prob. If we put a
            punctuation sign, we add it to the sentence according to a format (example : 'ps'). The format is chosen
            according to punctuation_format_distribution.
        """
        min_length = self.min_length_distribution.sample()
        sentence = Sentence(components=list())
        while sentence.length < min_length:
            word = self.word_generator.sample()
            sentence.append(word)

            put_punctuation = self._get_put_punctuation()
            punctuation_formatted = []
            if put_punctuation:
                punctuation_sign = self.punctuation_sign_distribution.sample()
                punctuation_format = self.punctuation_format_distribution.sample()
                for c in punctuation_format:
                    if c == 's':
                        punctuation_formatted.append(Separator([self.separator, ]))
                    elif c == 'p':
                        punctuation_formatted.append(Punctuation([punctuation_sign, ]))

            if put_punctuation:
                for c in punctuation_formatted:
                    sentence.append(c)
            else:
                sentence.append(Separator([self.separator,]))

        return sentence

    def _get_put_punctuation(self):
        """returns (x) that takes values (False, True) so that P(x=True) = self.punctuation_prob and
        P(x=False) = (1 - self.punctuation_prob).  (Bernoulli Distribution)"""
        return random.random() < self.punctuation_prob

