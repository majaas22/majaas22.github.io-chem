
import numpy as np
import matplotlib.pyplot as plt

A0 = 1.0   # concentration A
B0 = 0.0   # concentration B
k1 = 0.7   # rate constant forward reaction
k2 = 0.3   #rate constant reverse reaction
steps = 20 # total time
dt = 0.1  # time step

time = np.arange(0, steps + dt, dt)
A =  np.zeros(len(time))
B = np.zeros(len(time))
A[0] = A0
B[0] = B0

for i in range(1, len(time)):
    dA = (-k1 * A[i-1] + k2 * B[i-1]) * dt
    dB = (k1 * A[i-1] - k2 * B[i-1]) * dt
    A[i] = A[i-1] + dA
    B[i] = B[i-1] + dB

plt.plot(time, A, label= '[A]')
plt.plot(time, B, label= '[B]')
plt.xlabel('Time / min')
plt.ylabel('Concentration / mol dm⁻³')
plt.title('Simulation of A ⇌ B')
plt.grid(True)
plt.legend()

plt.show()