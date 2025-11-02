print("hello")
import numpy as np
import matplotlib.pyplot as plt

def unit_step_function(t):
    #creates a function that returns 1 when t>=0 and returns 0 elsewhere
    return np.where(t>0, 1, 0)
    
t = np.linspace(-10,20)
u = unit_step_function(t)



plt.plot(t,u)
plt.show()

