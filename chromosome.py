from random import randint

max_length = 8

class bitarray_chromosome():
    genome = [0] * max_length
    
    def __init__(self, genes = ()):
        l = len(self.genome)
        self.genome = genes[0:l] + self.genome[len(genes):]
    
    def fitness(self):
        return sum(self.genome) 
        
    def mutate(self):
        index = randint(0, max_length-1)
        self.genome[index] ^= 1
        return self

    def __repr__(self):
        return "bitarray_chromosome([" + ", ".join([str(i) for i in self.genome])+"]" + ")"

    def __add__(self, other):
        try:
            if (len(self.genome) != len(other.genome)):
                return NotImplemented
        # one-point crossover
            index = randint(0, max_length)
            return bitarray_chromosome(self.genome[:index] + other.genome[index:])
        except AttributeError:
            return NotImplemented
        
def random_bitarray_chromosome():
    return bitarray_chromosome([randint(0, 1) for i in range(max_length)])