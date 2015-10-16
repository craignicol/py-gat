from chromosome import chromosome, random_chromosome

def test_initialiser_correct_length():
    g = (1, 1, 1, 1, 1, 1, 1, 1)
    c = chromosome(g)
    assert(c.genome == g)

def test_initialiser_too_long():
    g = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    c = chromosome(g)
    assert(c.genome == (1, 1, 1, 1, 1, 1, 1, 1))

def test_initialiser_too_short():
    g = (1, 1, 1, 1, 1, 1)
    c = chromosome(g)
    assert(c.genome == (1, 1, 1, 1, 1, 1, 0, 0))

def test_fitness():
    assert(chromosome((0, 0, 0, 0, 0, 0, 0, 0)).fitness() == 0)
    assert(chromosome((0, 0, 0, 0, 0, 0, 0, 1)).fitness() == 1)
    assert(chromosome((0, 0, 0, 0, 0, 0, 1, 1)).fitness() == 2)
    assert(chromosome((0, 0, 0, 0, 0, 1, 1, 1)).fitness() == 3)
    assert(chromosome((0, 0, 0, 1, 1, 1, 1, 0)).fitness() == 4)
    assert(chromosome((1, 1, 1, 1, 1, 0, 0, 0)).fitness() == 5)
    assert(chromosome((0, 0, 1, 1, 1, 1, 1, 1)).fitness() == 6)
    assert(chromosome((1, 1, 1, 1, 1, 0, 1, 1)).fitness() == 7)
    assert(chromosome((1, 1, 1, 1, 1, 1, 1, 1)).fitness() == 8)
    
def test_random_chromosome():
    assert(max([random_chromosome().fitness() for i in range(1000)]) <= 8)