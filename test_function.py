print("hello")
import numpy as np
import matplotlib.pyplot as plt


#Testing square wave function
from signals_and_systems import square_wave   
t = np.linspace(0,10,100)
y = square_wave(t, period=1)
assert y[1] == 1

#Testing unit step function
from signals_and_systems import unit_step_function
t = np.linspace(-10,20)
u = unit_step_function(t)

assert u[19] == 1


#Testing time-shifted square wave function


#Testing time-shifted unit step function

#Testing time-scaled square wave function

#Testing time-scaled unit step function





