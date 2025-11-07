print("hello")
import numpy as np
import matplotlib.pyplot as plt
from signals_and_systems import square_wave, unit_step_function, create_sine_wave

#Testing the sine wave function
def test_create_sine_wave():
    t, y = create_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0

    t, y = create_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = create_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0

    t, y = create_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)
print("create_sine_wave() test passed.\n")


#Testing square wave function
def test_square_wave_function() :
    t = np.linspace(0,10,100)
    y = square_wave(t, period=1)
    assert len[y] == len[t]
    assert set(np.unique(y)).issubset({-1, 1})
print("square_wave() test passed.\n")

#Testing unit step function
def test_unit_step_function() :
    t = np.array([-2,-1,0,1,2])
    expected_output = [0,0,1,1,1] # u(t)=0 for t<0 and u(t)=1 for t>=0
    assert np.all_equal(unit_step_function, expected_output) #checks if the unit step function yields the same output as the expected_output 
print("unit_step_function() test passed.\n")







