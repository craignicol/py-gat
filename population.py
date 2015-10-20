class population():
    pop = []
    
    def __init__(self, size, generator):
        self.pop = [generator() for i in range(size)]