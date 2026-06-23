import numpy as np
import matplotlib.pyplot as plt 

A0 = 1.0   # concentration A
B0 = 0.0   # concentration B
C0 = 0.0   # concentration C

R = 8.314 # gas constant in J/(mol*K)
T = 400 # temperature in Kelvin [350,375,400]

Ea1 = 50000 # Activation energy forward reversible reaction in J/mol
Ea2 = 55000 # Activation energy reverse reversible reaction in J/mol
Ea3 = 55000 # Activation energy forward irreversible reaction in J/mol

A1 = 1e6   # Pre-exponential factor forward reversible reaction in min⁻¹
A2 = 1e7   # Pre-exponential factor reverse reversible reaction in min⁻¹
A3 = 1e7   # Pre-exponential factor forward irreversible reaction in min⁻¹

k1 = A1 * np.exp(-Ea1 / (R * T))  # rate constant forward reversible reaction 
k2 = A2 * np.exp(-Ea2 / (R * T))  # rate constant reverse reversible reaction 
k3 = A3 * np.exp(-Ea3 / (R * T))  # rate constant forward irreversible reaction B → C

steps = 100 # total time in minutes 
dt = 0.01  # time step

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