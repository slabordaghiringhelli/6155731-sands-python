print("Hello!")


import numpy as np
import matplotlib.pyplot as plt



def create_sine_wave(frequency, duration):
    """This function yields a sine wave for a given frequency and duration"""
    t = np.linspace(0, duration, int(44100 * duration))
    return np.sin(2 * np.pi * frequency * t)
    


sine_wave = create_sine_wave(1, 2)



plt.plot(sine_wave)
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude")
plt.title("Sine wave")
plt.show()

print("hello")

#Unit step function

def unit_step_function(t):
    """creates a function that returns 1 when t>=0 and returns 0 elsewhere"""
    return np.where(t>0, 1, 0)
    
t = np.linspace(-10,20)
u_values = unit_step_function(t)





#Periodic square wave function

def square_wave(t, period=1) :
    """Creates a periodic square wave function.
     The time has been defined using an np.linspace() function from 0 to 10 using a 100 points in that aforementioned interval."""
    t = np.linspace(0,10,100)
    t_periodic = t % 1  #Here I ensure that the time in the function is periodic
    return np.where(t_periodic<period/2,1,-1)
y = square_wave(t, period=1)   


plt.plot(t,y)
plt.show()



#Time scaling

u_new = unit_step_function(t-2)

plt.plot(u_new)
plt.show()


t_shift = 2

y_new = -2*square_wave(t-t_shift, period=1)

plt.plot(t, y_new)
plt.ylim(-3,3)
plt.show()


#Multiplication of two different functions

z = unit_step_function(t)*y
plt.plot(t,z)
plt.title("z=u(t)·y")
plt.xlabel("time/t")
plt.ylabel("z")
plt.xlim(0,5)
plt.show()