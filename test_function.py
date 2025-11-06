print("hello")
import numpy as np
import matplotlib.pyplot as plt




def square_wave(t, period=1) :
    t_periodic = t % 1  #Here I ensure that the time in the function is periodic
    return np.where(t_periodic<period/2,1,-1)
t = np.linspace(-5,5,1000)
y = square_wave(t, period=1)   

y = square_wave(t, period=1)
assert y[1] == 1



def unit_step_function(t):
    #creates a function that returns 1 when t>=0 and returns 0 elsewhere
    return np.where(t>0, 1, 0)
    
t = np.linspace(-10,20)
u = unit_step_function(t)

assert u[19] == 1







