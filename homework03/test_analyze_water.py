from analyze_water import calc_turb, calc_time
import pytest

def test_calc_turb():
    assert calc_turb([{'a0': 0.5, 'I90': 1.1}], 'a0', 'I90', 0) == 0.55 # checks calc_turb calculate correctly
    assert isinstance(calc_turb([{'a0': 0.5, 'I90': 1.1}], 'a0', 'I90', 0), float) == True # checks calc_turb return float


def test_calc_time():
    assert calc_time(10) == 113.97408559184939 # checks calc_time calculate correctly
    assert isinstance(calc_time(10), float) == True # checks calc_time return float

def test_excep_calc_turb():
    with pytest.raises(KeyError):
        calc_turb([{'a0': 0.5, 'I90': 1.1}], 'no', 'no', 0) # key strings don't exist in the dict
    with pytest.raises(TypeError):
        calc_turb([{'a0': 0.5, 'I90': 'x'}], 'a0', 'I90', 0) # string invalid value type
    with pytest.raises(IndexError):
        calc_turb([{'a0': 0.5, 'I90': 1.1}], 'a0', 'I90', -5) # list item number in index of list

def test_excep_calc_time():
    with pytest.raises(ValueError):
        calc_time(-1) # no negative input
    with pytest.raises(ZeroDivisionError):
        calc_time(0) # no input of 0
    with pytest.raises(TypeError):
        calc_time('string') # no string input
