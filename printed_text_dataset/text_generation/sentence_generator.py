import random

from printed_text_dataset.text_generation.generator import _Generator
from printed_text_dataset.text_generation.word_generator import WordGenerator

class SentenceGenerator(_Generator):
    """A class that generates sentences through calling the function sample()"""
    def __init__(self, word_generator : WordGenerator, length_distribution, punctuation_signs, punctuation_prob,
                 punctuation_sign_distribution, separator=" ", punctuation_format=["sps", "ps", "sp"],
                 punctuation_format_distribution=[1/3, ] * 3):
        """word_generator : an instance of the class word_generator.WordGenerator that is used to generate words

        length_distribution : A list of integers that represents the probability of each length to be chosen during
        sampling. Example : [0.7, 0.1, 0.2] means the sentence has a minimum length of 1 character with a probability of
        0.7. While generating the sentence, when this minimum length is first reached or surpassed, the generation
        stops.

        punctuation_signs : A list that contains the characters that act as punctuation signs

        punctuation_prob : It's the probability of the presence of a punctuation sign between two consecutive words

        punctuation_distribution : A list of integers that represents the probability of each punctuation sign
        to be chosen during the generation of the sentence

        separator : A String of characters that separates two consecutive words in the sentence. default = ' '

        punctuation_format : The format used to write punctuation default : ['sps', 'ps', 'sp']. 'sps' means that when
        we put punctuation we want to put first a separator (s) then the sign of punctuation (p) then another separator
        (s)

        punctuation_format_distribution : A list of integers that represents the probability of each punctuation format
        to be chosen during sampling. default : [1/3, 1/3, 1/3]
        """
        super().__init__()
        self.word_generator = word_generator
        self.length_distribution = length_distribution
        self.separator = separator
        self.punctuation_signs = punctuation_signs
        self.punctuation_prob = punctuation_prob
        self.punctuation_sign_distribution = punctuation_sign_distribution
        self.punctuation_format = punctuation_format
        self.punctuation_format_distribution = punctuation_format_distribution

    def sample(self):
        """Generates a sentence. Returns a list of characters"""
        min_length = self._get_random_min_length()
        sentence = []
        while True:
            put_punctuation = self._get_put_punctuation()
            word = self.word_generator.sample()
            punctuation_formatted = []
            if put_punctuation:
                punctuation_sign = self._get_random_punctuation_sign()
                punctuation_format = self._get_random_punctuation_format()
                for c in punctuation_format:
                    if c == 's':
                        punctuation_formatted.append(self.separator)
                    elif c == 'p':
                        punctuation_formatted.append(punctuation_sign)

            if put_punctuation:
                sentence.append(word)
                sentence.append(punctuation_formatted)
            else:
                sentence.append(word)
                sentence.append(list(self.separator))
            if len(sentence) > min_length:
                break

        return sentence

    def _get_put_punctuation(self):
        return random.random() < self.punctuation_prob

    def _get_random_min_length(self):
        return random.choices(range(1, len(self.length_distribution) + 1), self.length_distribution)[0]

    def _get_random_punctuation_sign(self):
        return random.choices(self.punctuation_signs, self.punctuation_sign_distribution)[0]

    def _get_random_punctuation_format(self):
        return random.choices(self.punctuation_format, self.punctuation_format_distribution)[0]

