import numpy as np
import matplotlib.pyplot as plt
from  signals_and_systems import create_sine_wave


sine_wave_1 = create_sine_wave(2,2)
sine_wave_2 = create_sine_wave(5,2)
sine_wave_3 = create_sine_wave(8,2)
sine_wave_4 = create_sine_wave(1,4)


plt.figure()
plt.xlim((0,30000))
plt.plot(sine_wave_1, label="sine wave 1")
plt.plot(sine_wave_2, label="sine wave 2")
plt.plot(sine_wave_3, 'g:', label="sine wave 3")
plt.plot(sine_wave_4, 'r:', label="sine wave 4")
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude")
plt.title("sine waves plotted")
plt.legend()
plt.show()



print("hello") 

print("Sergi is testing")

from signals_and_systems import unit_step_function
from signals_and_systems import square_wave


#Time shifting for the unit step function
t = np.linspace(-10,20)
u_new = unit_step_function(t-2)
plt.plot(u_new)
plt.show()


#Time shifting for the square wave function
t = np.linspace(0,10,100)
y = square_wave(t, period=1)
t_shift = 2

y_new = -2*square_wave(t-t_shift, period=1)

plt.plot(t, y_new)
plt.xlabel()
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


#Time scaling for the unit step function

u_scaled = unit_step_function(2*t) 

plt.plot(t, u_scaled)
plt.title("scaled unit step function")
plt.xlabel("time/t")
plt.ylabel("u(2t)")
plt.xlim(-5,5)
plt.show()


#Time scaling for the square wave function
y_scaled = square_wave(2*t, period=5)
plt.plot(y_scaled)
plt.title