from printed_text_dataset.text_generation.generator import _Generator
import random


class Distribution(_Generator):
    """A class to represent discrete distribution.
    The attribute prob_dict contains the probabilities.
    An instance of this class can generate samples according to 'prob_dict'"""
    def __init__(self, prob_dict : dict):
        """prob_dict : This is a dictionary that contains couples (key, value) where:
        - key : represents a value that could take the random variable associated to this distribution.
        - value : is the probability of the apparition of the key
        To summarize : P(x = key) = value ; for each (key, value) in prob_dict
        The sum of keys is not forced to be 1. (use random.choices function).

        _keys : The keys of 'prob_dict' in form of a list
        _values : The values of 'prob_dict' in form of a list

        NOTE : _keys and _values were added to avoid calculating list(prob_dict.keys()) and list(prob_dict.values())
        at each call of the function sample()"""

        super().__init__()
        self.prob_dict = prob_dict
        self._keys = list(prob_dict.keys())
        self._values = list(prob_dict.values())

    def sample(self):
        return random.choices(self._keys, self._values, k=1)[0]
