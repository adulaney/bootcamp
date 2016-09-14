import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import scipy.stats
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize':18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Exercise 3.3

# specify parameter
k = 1

# Set time step
delta_t = 0.01

# Make array of time points
t = np.arange(0,10,delta_t)

# Make an array to store the number of bacteria
n = np.empty_like(t)

# set initial condition
n[0] = 1

# Write loop to update n
for i in range(1, len(t)):
    n[i] = n[i-1] + delta_t * k * n[i-1]

plt.plot(t,n)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of bacteria')
plt.close()

"""
Fox - Rabbit Population Growth
"""

# initial conditions
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
dt = 0.0001
t = np.arange(0,60,dt)

# Initialize populations
r = np.empty_like(t)
f = np.empty_like(t)
r[0] = 10
f[0] = 1

for i in range(1,len(t)):
    r[i] = r[i-1] + (alpha * r[i-1] - beta * r[i-1] * f[i-1]) * dt
    f[i] = f[i-1] + (delta * f[i-1] * r[i-1] - gamma * f[i-1]) * dt

# Using Scipy ODE solver
def rabbit_pop(y, t):
    alpha = 1
    beta = 0.2
    delta = 0.3
    gamma = 0.8
    rab, fox = y
    dydt = [alpha * rab - beta * fox * rab, delta * fox * rab - gamma * fox]
    return dydt

sol = scipy.integrate.odeint(rabbit_pop, [10,1], t)

# Plot
plt.plot(t,r)
plt.plot(t,f)
plt.plot(t,sol[:,0])
plt.plot(t,sol[:,1])
plt.xlabel('time')
plt.ylabel('Animal Population')
plt.legend(('Rabbits','Foxes', 'Rabbit Scipy', 'Fox Scipy'),loc='best')
plt.show()
