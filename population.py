import random

class population():
    pop = []
    
    def __init__(self, size, generator):
        self.pop = [generator() for i in range(size)]
        
    def select_two_members(self):
        return random.sample(self.pop, 2)
    
    def run_once(self):
        "Run one iteration of the genetic algorithm"
        # Use replacement algorithm
        new_pop = []
        for i in range(len(self.pop)):
            a, b = self.select_two_members()
            new_pop.append(a + b)
        self.pop = new_pop