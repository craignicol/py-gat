from random import randint

max_length = 8

class bitarray_chromosome():
    genome = [0] * max_length
    
    def __init__(self, genes = ()):
        l = len(self.genome)
        self.genome = genes[0:l] + self.genome[len(genes):]
    
    def fitness(self):
        return max_length-sum(self.genome) 
        
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

def bool2double(bitarray, rangemin, rangemax):
    if rangemax < rangemin:
        rangemin, rangemax = rangemax, rangemin
    raw_int_value = sum([a * b for (a,b) in zip([2**i for i in range(max_length)][::-1], bitarray)])
    full_range = rangemax - rangemin
    return rangemin + (raw_int_value * full_range)/(2**max_length - 1)
    
class dj1_chromosome(bitarray_chromosome):
    ## Use PGA offsets for functions where global maxima occurs at the origin
    # offset = 0.053    
    ## Standard Offset
    offset = 0
    
    rangemax = 5.12
    rangemin = -rangemax
      
    def __repr__(self):
        return "dj1_chromosome([" + ", ".join([str(i) for i in self.genome])+"]" + ")"

    def fitness(self):
        var_size = max_length//3
        
        n1 = bool2double(self.genome[0:var_size], self.rangemin, self.rangemax) + self.offset
        n2 = bool2double(self.genome[var_size:2*var_size], self.rangemin, self.rangemax) + self.offset
        n3 = bool2double(self.genome[2*var_size:], self.rangemin, self.rangemax) + self.offset
        
        return n1**2 + n2**2 + n3**2
        
def random_dj1_chromosome():
    return dj1_chromosome([randint(0, 1) for i in range(max_length)])
