from printed_text_dataset.text_generation.generator import _Generator
import random


class Distribution(_Generator):
    def __init__(self, prob_dict : dict):
        super().__init__()
        self.prob_dict = prob_dict
        self._keys = list(prob_dict.keys())
        self._values = list(prob_dict.values())

    def sample(self):
        return random.choices(self._keys, self._values, k=1)[0]