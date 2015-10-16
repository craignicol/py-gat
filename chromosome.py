import random

class chromosome():
    genome = (0, 0, 0, 0, 0, 0, 0, 0)
    
    def __init__(self, genes = ()):
        self.genome = genes[0:8]
    
    def fitness(self):
        return sum(self.genome) 
        
