from population import population
from ordered_population import ordered_population
from chromosome import random_bitarray_chromosome

def get_random_population(size):
    return population(size, random_bitarray_chromosome)
    
def get_random_ordered_population(size):
    return ordered_population(size, random_bitarray_chromosome)

rp = get_random_population(5)
op = get_random_ordered_population(5)