---
title: Ab initio methods in solid state physics
subtitle: "IX. Lattice dynamics - harmonic approximation"
author: "*Przemysław Piekarz and Paweł T. Jochym*"
format:
  beamer:
    fontsize: 10pt
    fontfamily: libertine
include-in-header: "aux/affil.tex"
aspectratio: 1610
theme: Madrid
date: last-modified
date-format: long
output-file: "Ab_initio_lecture_09"

---


## Lattice dynamics
* Atoms vibrate $\rightarrow$ lattice vibrations $\rightarrow$ thermodynamics 
* Lattice dynamics:[^AAM][^BH]
    - heat conductance
    - heat capacity
    - thermodynamic stability
    - mechanical stability
    - phase transitions
    - thermoelectricity    


[^AAM]: A. A. Maradudin, *Theory of Lattice Dynamics in the Harmonic Approximation* / (New York :, 1963.).
[^BH]: M. Born and K. Huang, *Dynamical Theory of Crystal Lattices* (Oxford University Press, 1988).

## Energy of the crystal



Atomic positions in crystal lattice are described by the position vector $\mathbf{R}(\mathbf{n}, i)$: 
$$
    \mathbf{R}(\mathbf{n}, i) = n_a \mathbf{a} + n_b \mathbf{b} + n_c \mathbf{c} + \mathbf{r}_i
$$
where $i$ numbers atoms in the primitive unit cell and vector of integers $\mathbf{n}=[n_a, n_b, n_c]$ numbers unit cells in the lattice while $\mathbf{r}_i$ is a position of the $i$-th atom relative to the origin of the unit cell with cell vectors $\mathbf{a}, \mathbf{b}, \mathbf{c}$.
Symmetry operations of the lattice act only on indexes $i, j, k, \ldots$, while the periodicity is encapsulated in the integer vector $\mathbf{n}$ and lattice vectors  $\mathbf{a}, \mathbf{b}, \mathbf{c}$.

Potential energy of the lattice can be expanded as a function of the atomic displacements $s_{n i\alpha}$, where $\alpha=x,y,z$, (assuming small vibrations and negligible in quantum effects): 
$$
      V(s) = V_0 + \sum_{n i \alpha}
      \left. \frac{\partial V}{\partial s_{n i\alpha}}\right|_{s=0} 
      s_{n i\alpha} + 
    \frac{1}{2}\sum_{n i\alpha}\sum_{n' i'\alpha'}
        \left. \frac{\partial^2 V}{\partial s_{n i\alpha}\partial s_{n' i'\alpha'}}\right|_{s=0} s_{n i\alpha} s_{n' i'\alpha'} + O(s^3)
$$

The linear term vanishes due to the equilibrium point assumption and we neglect higher order terms assuming they are small.

## Equation of motion

We can now write the Lagrangean $L=T-V$ and the Euler-Lagrange equation:
$$
\frac{d}{dt}\frac{\partial L}{\partial\dot{s}_{n i\alpha} }=
\frac{\partial L}{\partial s_{n i\alpha} }
$$

resulting in the equation of motion:
$$
m_i \ddot{s}_{n i\alpha} = - \sum_{n' i'\alpha'} 
    \Phi_{n i\alpha}^{n' i'\alpha'} s_{n' i'\alpha'} 
$$

where we have introduced force constants matrix $\Phi$ denoting the second derivative term:
$$
\Phi_{n i\alpha}^{n' i'\alpha'}=\left.\frac{\partial^2 V(s)}{\partial s_{n i\alpha}\partial s_{n' i'\alpha'}}\right|_{s_{n i\alpha}=0}
$$
Obviously, $\Phi_{n i\alpha}^{n' i'\alpha'}=\Phi_{n' i'\alpha'}^{n i\alpha}$ is symmetric. 

## Solution of EOM

We can search for the solution of EOM with the standard oscillating ansatz:
$$
s_{n i\alpha}(t)=\frac{1}{\sqrt{m_i}}u_{n i\alpha} e^{-i\omega t}
$$
The equation of motion now takes form of eigen-equation:
$$
\omega^2 u_{n i\alpha} = \sum_{n' i'\alpha'} 
    \Phi_{n i\alpha}^{n' i'\alpha'} u_{n' i'\alpha'} 
$$

Note that the interaction between atoms ${n i\alpha}$ and ${n' i'\alpha'}$ depend only on relative positions of unit cells $n$ and $n'$.
Thus, we can select arbitrary unit cell for the origin and consider one of the indexes constant $n'=0$ and replace $\Phi_{n i\alpha}^{n' i'\alpha'}$ with $\Phi_{i\alpha}^{i'\alpha'}(n)$ taking care of the translational symmetry of the crystal.

## Dynamical matrix

We can further simplify the solution by taking into account the periodicity of the crystal lattice and taking another ansatz for a solution -- this time oscillating in spatial coordinates with wave vector $\mathbf{q}$:
$$
u_{n i\alpha}=\varepsilon_{i\alpha}e^{i\mathbf{q}\cdot\mathbf{R}_n}
$$
where $\mathbf{R}_n$ denotes relative positional vector of the $n^\mathrm{th}$ unit cell and $\mathbf{q}$ is the point in the first Brillouin zone.

Finally, the equation of motion takes form of eigenequation:
$$
\omega^2(\mathbf{q}) \varepsilon_{i\alpha} = 
    \sum_{i'\alpha'} D_{i\alpha}^{i'\alpha'}(\mathbf{q}) \varepsilon_{i'\alpha'}
$$
where dynamical matrix $D$ is defined by the equation:
$$
D_{i\alpha}^{i'\alpha'}(\mathbf{q}) = 
    \sum_{n} \frac{\Phi_{i\alpha}^{i'\alpha'}(n)}
                    {\sqrt{m_i m_{i'}}}
    e^{i\mathbf{q}\cdot\mathbf{R}_n}
$$
above and $\varepsilon_{i\alpha}$ present themselves as eigenvectors of the dynamical matrix -- i.e. polarisation vectors or normal base vectors.

## Force constants

Atomic displacements $s_{n i\alpha}$ are connected with forces acting on atoms $F_{n i \alpha}$ with linear relation:

$$
F_{n i \alpha} = - \frac{\partial V}{\partial s_{n i\alpha}} =
      - \sum_{m j\beta} 
    \Phi_{n i\alpha}^{m j\beta} s_{m j\beta}
$$

This is again a linear force-displacement relation similar to the one we encountered while calculating elastic tensor in Lecture 8. And we can use similar trick to derive matrix $\Phi$ from sets of forces and displacements

Similar to the elastic tensor case the $\Phi$ matrix is subject to symmetries of a particular crystal. Unfortunately, here it is much more complicated. But still we can symbolically rewrite above relation as following large set $N$ of linear equations ($a=1 \ldots N$):
$$
F^a = S(s^a) I_\Phi 
$$
Where $a$ numbers set of displacements, $S(s^a)$ is a symmetry-encoding matrix which is a function of displacements and $I_\Phi$ is a set of independent parameters of $\Phi$. 

## Direct (Finite Displacements) method

The force-displacement relation can be approximately solved by fitting the $I_\Phi$ parameters to make the sides of the equation as close as possible in the least-squares sense.[^PLK] Again, we often use SVD for this, but this is by far not the only method of solving this problem (e.g. Elastic-net regression, Adaptive LASSO).[^TGT] [^ALAMODE]

The remaining problems are:
* Construction of the matrix $S(s^a)$ and vector $I_\Phi$
* Selection of displacement sets $s^a$
* Multiple subtle issues (supercell selection, exact points, etc.)

[^PLK]: K. Parlinski, Z. Q. Li, and Y. Kawazoe, Phys. Rev. Lett. 78, 4063 (1997)
[^TGT]: T. Tadano, Y. Gohda, and S. Tsuneyuki, J. Phys.: Condens. Matter 26, 225402 (2014)
[^ALAMODE]: [ALAMODE manual](https://alamode.readthedocs.io/en/latest/almdir/formalism_alm.html)

## Direct method in practice

* Construction of $S(s)$ is coded in multiple phonon-calculation programs (ALAMODE, PhonoPy, Phonon, Phon, GULP, ...)
* Selection of $I_\Phi$ follows directly from the $S$ matrix
* The same goes for the rest of computational details
* Selection of displacements:
    - Elementary displacements (minimal set: PhonoPy, Phonon, ...)
    - Random or thermodynamic displacements (ALAMODE, HECSS)
* Selection of the supercell:
    - Smallest cell containing interaction range
    - Preferably commensurate with important points in reciprocal space
    - Preferably not braking symmetry of the crystal


## Goals

* Frequencies $\omega(\mathbf{q})$
* Polarization vectors $\varepsilon$
* Density of states $p(\omega)$
* Structure stability
* Phase transitions
* Phonon heat capacity
