
Development Notes — Brownian Motion

This document records the development process of the project: the approaches tested, the problems encountered, and the decisions made to reach the current version. For an overview of the project and its results, see the README.

First Approach

In the first implementation, developed in Python, the idea was to represent the motion of a main particle based on the influence of other particles randomly distributed throughout space

The main particle remained as a reference for calculating its own position, while the other particles were generated at pseudorandom positions. At each step of the simulation, the distances between the main particle and the other particles were calculated

When a particle was sufficiently close to the main particle, its distance was used to determine the probability that it would influence the motion. If an interaction occurred, a directional contribution was added to the resulting motion, using the components `(cos(x), sin(y))`

The resultant of these contributions determined the displacement of the main particle during the following simulation step

Problems Encountered:

1 Computational Cost

The first implementation had a high computational cost. At each step, it was necessary to generate and analyze a large number of points (10,000+) and calculate their distances relative to the main particle. This approach required a large number of repetitive operations and was not an efficient way to represent the phenomenon

2 Graphics Library

The first version used the `Turtle` library to visually represent the particle's trajectory. I encountered compatibility and functionality issues in the macOS environment used during development, which motivated the search for a visualization tool better suited to numerical experiments

3 Conceptual Problem

The main problem, however, was not computational but conceptual. Although the model produced an apparently random trajectory, it did not properly correspond to the usual mathematical model of Brownian motion. The trajectory was a consequence of the artificial interaction rules I had defined, rather than a properly formulated Brownian stochastic process

I therefore realized that simply producing a random trajectory was not sufficient to characterize Brownian motion. The process itself had to correspond to the correct stochastic model

Changes Made:

Based on these problems, the project was reformulated

1 Computational Approach

I sought a simpler and more efficient approach, eliminating the need to explicitly calculate interactions between thousands of particles. I switched to a representation directly based on the random displacements of the particle itself, eliminating the need to explicitly simulate interactions between thousands of particles

2 Graphics Library

I replaced `Turtle` with `Matplotlib`, a library better suited to visualizing data and trajectories in numerical simulations due to its simplicity and suitability for scientific plotting

3 Mathematical Model

The main change was conceptual. Instead of attempting to produce Brownian motion through explicit interactions between multiple particles, I began modeling the particle's displacements using a normal distribution. Each component of the displacement is obtained from a Gaussian random variable, allowing a random walk consistent with the mathematical model used to represent Brownian motion

This change made the model both computationally simpler and closer to the mathematical formulation of the phenomenon:

def deslocax(x):
    x = x + math.sqrt(2 * D * t) * random.gauss(0, 1)
    return x

def deslocay(y):
    y = y + math.sqrt(2 * D * t) * random.gauss(0, 1)
    return y



Limitations and Next Steps:

1 Increase the number of simulated trajectories

2 Study the convergence of the MSD for different values of D, and construct an MSD × time plot comparing the simulation with the theoretical prediction 4Dt

3 Study the influence of the time step t on the simulation

4 Calculate the absolute error |MSD - 4Dt| and the relative error |MSD -4Dt|/4Dt (0, 1) for different values of D

5 Compare the histograms of the x and y displacements with the analytical Gaussian distribution

6 Optimize the code, as the current version becomes slow when simulating more than 5,000 particles

7 Explore the diffusion equation and estimate D from the simulated data

8 Extend the simulation to three dimensions, possibly using another visualization library

9 Produce a final animation of the trajectory
