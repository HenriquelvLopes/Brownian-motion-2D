Brownian-motion-2D

Simulation of two-dimensional Brownian motion in Python, using random Gaussian displacements and numerical comparison of the mean squared displacement (MSD) with the theoretical relation `MSD = 4Dt`.

About the Project:

This project consists of a computational simulation of Brownian motion in two dimensions. The idea is to represent a particle subjected to random displacements and numerically investigate statistical properties characteristic of the phenomenon — particularly, the relationship between the mean squared displacement (MSD) and time.

I chose a simple Brownian motion model as a starting point for my studies on the subject, before moving on to more complete formulations, such as the Langevin equation, which explicitly includes effects such as drag and random forces.

## Model

At each time step, the particle's displacements in the `x` and `y` directions are sampled from a normal distribution:

$$
\Delta x = \sqrt{2D\Delta t}\,\xi_x
\qquad
\Delta y = \sqrt{2D\Delta t}\,\xi_y
$$

where

$$
\xi_x,\xi_y \sim \mathcal{N}(0,1).
$$

The particle's position is then updated according to the Brownian diffusion model:

$$
x_{t+\Delta t}=x_t+\Delta x
$$

$$
y_{t+\Delta t}=y_t+\Delta y
$$

As a verification of the model's behavior, I numerically compare the mean squared displacement with the theoretical relation expected for the two-dimensional case:

$$\mathrm{MSD}(t) = \left\langle (x(t)-x_0)^2+(y(t)-y_0)^2 \right\rangle = 4Dt$$

Therefore, for a constant diffusion coefficient, the MSD is expected to grow linearly with time.

Results

The simulation produces an irregular trajectory characteristic of a Brownian process.

The mean squared displacement exhibits approximately linear growth with time, in agreement with the theoretical relation `MSD = 4Dt`.

The plots below will be updated as the numerical experiments are further refined.

Requirements: Python 3.x NumPy Matplotlib

```bash
pip install numpy matplotlib
```

How to Run:

```bash
python brownian_motion.py
```

Development:

The current model represents the simplest case of Brownian diffusion, without the explicit inclusion of a drag term.

The identified limitations and planned next steps — such as studying MSD convergence, the influence of the time step, extending the model to three dimensions, and comparing the results with the analytical Gaussian distribution — are detailed in [`DEVELOPMENT.md`](./DEVELOPMENT.md).

Historical Reference:

The original formulation of the problem, including the theoretical prediction relating the observable displacement of suspended particles to thermal molecular motion, can be found in Einstein's 1905 paper:

Einstein, A. (1905). *On the Movement of Small Particles Suspended in Stationary Liquids Required by the Molecular-Kinetic Theory of Heat*. Annalen der Physik, 17, 549–560.

[English translation (UConn Math)](https://www2.math.uconn.edu/~gordina/Einstein_Brownian1905.pdf)

Introductory Reference:

Philipse, A. P. (2011). *Notes on Brownian Motion*. Utrecht University.

[Notes on Brownian Motion (PDF)](https://userpages.umbc.edu/~dfrey1/ench630/philipse_notes_on_brownian_motion.pdf)

Mathematical Reference:

Stewart, J. *Cálculo, Volume II*. Cengage Learning.


