from printed_text_dataset.text_generation.generator import _Generator
import random


class Distribution(_Generator):
    def __init__(self, prob_dict : dict):
        super().__init__()
        self.prob_dict = prob_dict

    def sample(self):
        return random.choices(self.prob_dict.keys(), self.prob_dict.values(), k=1)[0]