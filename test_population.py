from population import population
from random import randint

import pytest

def test_generator_creates_enough_members():
    p = population(100, lambda : randint(0, 100))
    assert(len(p.pop) == 100)