from population import population
from chromosome import random_bitarray_chromosome

def get_random_population(size):
    return population(size, random_bitarray_chromosome)
    
