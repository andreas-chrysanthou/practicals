# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt

# Function defining the initial and boundary 
def initialBell(x):
    return np.where(x %1.<0.5,np.power (np.sin(2 * x * np.pi),2),0)

#Setup space, initial phi profile and Courant number
nx = 40 # Number of points in space
c = 0.2 # The Courant number

# Spatial variable spanning from zero to one inclusive
x = np.linspace (0.0, 1.0, nx+1)
# Tree time levels of the dependent variable, phi
phi = initialBell(x)
phiNew = phi.copy()
phiOld = phi.copy()
phi2 = initialBell(x)
phiNew2 = phi.copy()
phiOld2 = phi.copy()

# FTCS for the first time−step
# loop over space

for j in xrange(1, nx):
    phi[j] = phiOld[j] - 0.5 *c*(phiOld[j+1] - phiOld[j-1])
    phi2[j] = phiOld2[j] - 0.5 *c*(phiOld2[j+1] - phiOld2[j-1])
# apply periodic conditions
phi[0]= phiOld[0] - 0.5*c*(phiOld[1] - phiOld[nx-1])
phi[nx] = phi[0]

#Loop over remaining time-steps (nt) using CTCS
nt=40

for n in xrange (1,nt):
# loop over space
    for j in xrange (1 ,nx):
        phiNew[j] = phiOld[j] - c*(phi[j+1] - phi [j-1])
        
        # apply periodic boundary conditions
        phiNew[0] = phiOld[0] - c*(phi[1] - phi[nx-1])
        phiNew[nx] = phiNew[0]
        
        # update phi for the next time-step
        phiOld = phi.copy( )
        phi = phiNew.copy( )


#Loop over remaining time-steps (nt) using FTCS

for n in xrange (1,nt):
# loop over space
    for j in xrange (1 ,nx):
        phiNew2[j] = phiOld2[j] - 0.5*c*(phi[j+1] - phi[j-1])
        
        # apply periodic boundary conditions
        phiNew2[0] = phiOld2[0] - 0.5*c*(phi[1] - phi[nx-1])
        phiNew2[nx] = phiNew2[0]
        
        # update phi for the next time-step
        phiOld2 = phi.copy( )
        phi2 = phiNew2.copy( )

# derived quantities
u = 1.
dx = 1./nx
dt = c*dx/u
t = nt*dt

# Plot the solution in comparison to the analytic solution
plt.plot (x,initialBell(x - u* t), 'k' ,label= 'analytic' )
plt.plot (x,phi, 'b', label = 'CTCS')
plt.plot (x,phi2, 'r', label = 'FTCS')
plt.legend (loc='best')
plt.xlabel ('x')
plt.ylabel ('$\phi$')
plt.axhline (0 ,linestyle=':', color='black')
plt.show( )
