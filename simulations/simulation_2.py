import numpy as np
import matplotlib.pyplot as plt 

A0 = 1.0   # concentration A
B0 = 0.0   # concentration B
C0 = 0.0   # concentration C
k1 = 0.7   # rate constant forward reversible reaction 
k2 = 0.3   # rate constant reverse reversible reaction 
k3 = 0.5   # rate constant forward irreversible reaction B → C

steps = 20 # total time
dt = 0.1  # time step

time = np.arange(0, steps + dt, dt)
A =  np.zeros(len(time))
B = np.zeros(len(time))
C = np.zeros(len(time))
A[0] = A0
B[0] = B0
C[0] = C0

# euler's method
for i in range(1, len(time)):
    dA = (-k1 * A[i-1] + k2 * B[i-1]) * dt
    dB = (k1 * A[i-1] - k2 * B[i-1] - k3 * B[i-1]) * dt
    dC = (k3 * B[i-1]) * dt
    A[i] = A[i-1] + dA
    B[i] = B[i-1] + dB
    C[i] = C[i-1] + dC

plt.plot(time, A, label= '[A]')
plt.plot(time, B, label= '[B]')
plt.plot(time, C, label= '[C]')
plt.xlabel('Time / min')
plt.ylabel('Concentration / mol dm⁻³')
plt.title('Simulation of A ⇌ B → C')
plt.grid(True)
plt.legend()
plt.show()
