from chromosome import chromosome

def test_initialiser_correct_length():
    g = (1, 1, 1, 1, 1, 1, 1, 1)
    c = chromosome(g)
    assert(c.genome == g)

def test_initialiser_too_long():
    g = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    c = chromosome(g)
    assert(c.genome == (1, 1, 1, 1, 1, 1, 1, 1))

def test_fitness():
    c = chromosome()
    assert(c.fitness() == 0)