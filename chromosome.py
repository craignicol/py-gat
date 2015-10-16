import random

max_length = 8

class chromosome():
    genome = (0,) * max_length
    
    def __init__(self, genes = ()):
        l = len(self.genome)
        self.genome = genes[0:l] + self.genome[len(genes):]
    
    def fitness(self):
        return sum(self.genome) 
        
def random_chromosome():
    return chromosome(tuple(random.randint(0, 1) for i in range(max_length)))