import random

class population():
    pop = []
    population_mutation_rate = 0.01
    chromosome_mutation_rate = 0.1
    crossover_rate = 0.2
    
    def __init__(self, size, generator):
        self.pop = [generator() for i in range(size)]
        
    def select_two_members(self):
        return random.sample(self.pop, 2)
        
    def maybe_mutate(self):
        if random.random() < self.population_mutation_rate:
            random.sample(self.pop, 1)[0].mutate()
    
    def run_once(self):
        "Run one iteration of the genetic algorithm"
        # Use replacement algorithm
        new_pop = []
        for i in range(len(self.pop)):
            a, b = self.select_two_members()
            new_pop.append(a + b)
        self.pop = new_pop
        self.maybe_mutate()
        
    def run_generations(self, n):
        for i in range(n):
            self.run_once()
            
    def print_pop(self):
        print("\n".join([str(c) for c in self.pop]))
            
    def statistics(self):
        print("{0} members, with maximum fitness {1}".format(len(self.pop), max([c.fitness() for c in self.pop])))
        