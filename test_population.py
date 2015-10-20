from population import population
from chromosome import random_bitarray_chromosome
from random import randint

import pytest

def test_generator_creates_enough_members():
    p = population(100, lambda : randint(0, 100))
    assert(len(p.pop) == 100)
    
def get_random_population(size):
    return population(size, random_bitarray_chromosome)
    
def test_run_once_doesnt_change_population_size():
    p = get_random_population(100)
    p.run_once()
    assert(len(p.pop) == 100)
    
def test_run_once_changes_the_population():
    p = get_random_population(2)
    before = p.pop[:] # Copy data, not reference
    p.run_once()
    after = p.pop[:]
    assert(len(after) == len(before) == 2)
    assert(after[0] != before[0])
    assert(after[1] != before[1])
    
