import random

class WordGenerator:
    """A class that generates words through calling the function sample()"""
    def __init__(self, unicode_characters, length_distribution):
        """unicode_characters : The list of characters that will be used to generate the words
        length_distribution : A list of integers that represents the probability of each length to be chosen during
        sampling. Example : [0.7, 0.1, 0.2] means the word has a length of 1 with a probability of 0.7"""
        self.unicode_characters = unicode_characters
        self.length_distribution = length_distribution

    def sample(self):
        """Generates a random word and return a list that contains its characters"""
        word = [random.choice(self.unicode_characters) for _ in range(
                random.choices(range(1, len(self.length_distribution) + 1), self.length_distribution)[0])]
        return word

