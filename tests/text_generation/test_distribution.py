import unittest
from printed_text_dataset.text_generation.distribution import Distribution

class TestDistribution(unittest.TestCase):
    def test_sample(self):
        """Check the probabilistic properties of the distribution"""
        d = {1:0.2, 2:0.3, 3:0.1, 4:0.2, 5:0.2}
        count = {k:0 for k in d.keys()}
        distrib = Distribution(d)
        nb_iter = 200000
        eps = 0.005
        for _ in range(nb_iter):
            count[distrib.sample()] += 1

        for k in count:
            count[k] /= nb_iter
            self.assertAlmostEqual(d[k], count[k], delta=eps)

