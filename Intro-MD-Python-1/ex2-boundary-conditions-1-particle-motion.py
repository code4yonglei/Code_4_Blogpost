import numpy as np
import random

numAtoms = 16
boxLength = 10

np.random.seed(numAtoms)
positions = np.random.rand(numAtoms, 2)*boxLength # positions of all particles
velocities = np.random.rand(numAtoms, 2) - 0.5    # velocities of all particles

numSteps = 100
timeStep = 0.5

def update_positions(positions, velocities, timeStep):
	for iatom in range(numAtoms):
		for col in [0, 1]:
			positions[iatom, col] += timeStep * velocities[iatom, col]


############################ Code for Visualization ############################
 
from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
plt.xlim([0, boxLength])
plt.ylim([0, boxLength])
camera = Camera(fig)

colorsList = random.sample(range(1, numAtoms+1), k = len(positions) )
colors = colorsList

for istep in range(numSteps):
	plt.scatter(positions[:, 0], positions[:, 1], s=256, c=colors, cmap='plasma')
	camera.snap()
	update_positions(positions, velocities, timeStep)

animation = camera.animate()
animation.save('ex2-boundary-conditions-1-particle-motion.gif', writer = 'pillow', fps=64)
