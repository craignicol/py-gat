from chromosome import bool2double
import pytest

def test_zero_maps_to_zero():
    assert(bool2double([0, 0, 0, 0, 0, 0, 0, 0], 0, 100) == 0)
    
def test_all_ones_maps_to_max():
    assert(bool2double([1, 1, 1, 1, 1, 1, 1, 1], 0, 15) == 15)
    
def test_long_chromosomes_all_ones_maps_to_max():
    assert(bool2double([1]*256, 0, 100) == 100)