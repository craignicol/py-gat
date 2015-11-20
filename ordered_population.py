from population import population
from random import randint
from math import floor

class ordered_population(population):
    def select_by_rank(self):
        # assumes sorted list, with highest fitness at the end
        max_i = len(self.pop)
        rand_i = floor(
            randint(0, max_i ** (1.0/self.crossover_rate))
            ** self.crossover_rate
            )
        return self.pop[min(rand_i, max_i-1)]
    
    def select_two_members(self):
        # assumes sorted list, with highest fitness at the end
        return self.select_by_rank(), self.select_by_rank()
    
    def run_once(self):
        # Note, this super() formulation is Python3 only
        self.pop = sorted(self.pop, key = lambda c : c.fitness(), reverse=True)
        super().run_once()
        self.pop = sorted(self.pop, key = lambda c : c.fitness(), reverse=True)        
