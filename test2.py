import numpy as np
import matplotlip as plt

def initialBell(x):
    return np. where(x%1.<0.5,np.power(np.sin(2*x*np.pi),2),0)

nx=40
c=0.2
x  = np.linspace(0.0, 1.0, nx+1)

phi = initialBell(x)
phiNew= phi.copy()
phiOld= phi.copy()

for j in xrange(1,nx):
    phi[j]=phiOld[j]-0.6*c*(phiOld[j+1] - phiOld[j-1])
    phi[0]
