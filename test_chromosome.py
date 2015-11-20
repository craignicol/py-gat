from chromosome import bitarray_chromosome, random_bitarray_chromosome, dj1_chromosome
import pytest

def test_initialiser_correct_length():
    g = [1, 1, 1, 1, 1, 1, 1, 1]
    c = bitarray_chromosome(g)
    assert(c.genome == g)

def test_initialiser_too_long():
    g = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    c = bitarray_chromosome(g)
    assert(c.genome == [1, 1, 1, 1, 1, 1, 1, 1])

def test_initialiser_too_short():
    g = [1, 1, 1, 1, 1, 1]
    c = bitarray_chromosome(g)
    assert(c.genome == [1, 1, 1, 1, 1, 1, 0, 0])

def test_fitness():
    assert(bitarray_chromosome([0, 0, 0, 0, 0, 0, 0, 0]).fitness() == 8)
    assert(bitarray_chromosome([0, 0, 0, 0, 0, 0, 0, 1]).fitness() == 7)
    assert(bitarray_chromosome([0, 0, 0, 0, 0, 0, 1, 1]).fitness() == 6)
    assert(bitarray_chromosome([0, 0, 0, 0, 0, 1, 1, 1]).fitness() == 5)
    assert(bitarray_chromosome([0, 0, 0, 1, 1, 1, 1, 0]).fitness() == 4)
    assert(bitarray_chromosome([1, 1, 1, 1, 1, 0, 0, 0]).fitness() == 3)
    assert(bitarray_chromosome([0, 0, 1, 1, 1, 1, 1, 1]).fitness() == 2)
    assert(bitarray_chromosome([1, 1, 1, 1, 1, 0, 1, 1]).fitness() == 1)
    assert(bitarray_chromosome([1, 1, 1, 1, 1, 1, 1, 1]).fitness() == 0)
    
def test_dj1_fitness():
    assert(dj1_chromosome([0, 0, 0, 0, 0, 0, 0, 0]).fitness() > 0)
    assert(dj1_chromosome([1, 1, 1, 1, 1, 1, 1, 1]).fitness() > 0)
    
def test_random_chromosome():
    assert(0 <= max([random_bitarray_chromosome().fitness() for i in range(1000)]) <= 8)
    
def test_mutate():
    c = random_bitarray_chromosome()
    before = c.fitness()
    after = c.mutate().fitness()
    assert(abs(before - after) == 1)
    
def test_cant_add_int_to_chromosome():
    with pytest.raises(TypeError):
        random_bitarray_chromosome() + 1
        
def test_can_add_two_chromosomes():
    a = random_bitarray_chromosome()
    b = random_bitarray_chromosome()
    assert(0 < (a+b).fitness() <= 8)