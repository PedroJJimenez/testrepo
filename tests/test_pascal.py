import pytest
from numpy import pi
from pascal import binomial_expansion
import numpy as np

def test_pascal():
    for x in np.random.rand(5):
        for y in np.random.rand(5):
            for n in np.random.randint(1, 10, size=5):
                assert abs(binomial_expansion(x, y, n) - (x + y) ** n) < 1e-6

test_pascal()