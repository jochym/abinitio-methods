---
title: Ab initio methods in solid state physics
subtitle: "VIII. Mechanical properties: elasticity of crystals"
author: "*Przemysław Piekarz and Paweł T. Jochym*"
format:
  beamer:
    fontsize: 10pt
    fontfamily: libertine
include-in-header: "affil.tex"
aspectratio: 1610
theme: Madrid
date: last-modified
date-format: long
jupyter: python3
---

## Elastic constants

* Response to external forces
* Sound velocity
* Anisotropy
* Mechanical stability
* Mechanical properties 
* Some phase transitions
* Some thermodynamical properties

## Linear theory of elasticity 

Formulated in the XVIII and XIX century by Cauchy, Euler,
Poisson, Young and many other great mathematicians and 
physicists of that time.[^LL]

* Deformation vector: $u_i = x'_i - x_i$

* Deformation (strain) tensor:
$$
u_{ik} = \frac{1}{2}\left(\frac{\partial u_i}{\partial x_k} + \frac{\partial u_k}{\partial x_i} + 
\sum_l \frac{\partial u_l}{\partial x_i} \frac{\partial u_l}{\partial x_k}
\right)
$$

* For small deformations:
$$
u_{ik} = \frac{1}{2}\left(
\frac{\partial u_i}{\partial x_k} + \frac{\partial u_k}{\partial x_i}
\right)
$$


[^LL]: L.D. Landau, E.M. Lifszyc, *Theory of elasticity*, Elsevier (1986)

## Stress tensor for crystals

:::: {.columns}

::: {.column width="65%"}
* Stress tensor $\sigma_{ik}$ and total force ${\cal F}_i$:   
$$
{\cal F}_i = \int F_i dV = \int \frac{\partial \sigma_{ik}}{\partial x_k} = \oint \sigma_{ik} ds_k
$$

* Free energy of deformed crystal:  
$$
F = \frac{1}{2}\lambda_{ijkl} u_{ij} u_{kl}
$$

* Basic symmetry of the *tensor of elasticity moduli* $\lambda$ (i.e. 21 independent components):
    
$$
    \lambda_{ijkl} = \lambda_{jikl} = \lambda_{ijlk} = \lambda_{klij}
$$

* Crystal symmetries reduce the independent components further (e.g. from cubic:3, to  triclinic:18).

:::

::: {.column width="35%"}

![](Components_stress_tensor_cartesian.svg)
:::
[^1]
::::

[^1]: Wikmedia Commons, author: Sanpaz; [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0)



## Stress - strain relation

* The elasticity tensor inherits symmetries of the crystal and has some intrinsic symmetries of its own. Therefore, only a small number of its components are independent. This fact leads to customary representation of this entity in the form of the matrix with components assigned according to Voight's notation: 

$$
\lambda_{ijkl} \rightarrow C_{\alpha\beta}: 
(\alpha,\beta\in\{xx,yy,zz,yz,zx,xy\}=\{1,2,3,4,5,6\})
$$


**Warning**: $\lambda_{ijkl}$ is a three-dimensional tensor of rank 4; $C_{\alpha\beta}$ is **not** a sixth-dimensional tensor! 


* Genaralized Hook's law:

$$
\sigma_{ij} = \lambda_{ijkl} u_{kl} \rightarrow 
\sigma_\alpha = C_{\alpha\beta} u_{\beta}
$$

This formula simply states that the stress in the crystal
$\sigma_{ij}$ is a linear function of the strain $u_{kl}$
incurred by its deformation, and the elasticity tensor
$\lambda_{ijkl}$ is just a tensor proportionality coefficient. 

## Effect of crystal symmetries (I)

The Voight's convention makes presentation of elastic constants much
easier -since it is just a square table of numbers - it slightly
complicates algebraic procedures as we lose the simplicity of the tensor formalism. Every class of crystal implies, through its symmetry, a different number of independent elements in the $C_{ij}$ matrix.

For example, the cubic lattice has just three independent elements in
the elastic matrix: $C_{11}, C_{12}, C_{44}$, and the matrix itself has
the following shape:

$$\begin{aligned}
\left[\begin{array}{cccccc}
C_{11} & C_{12} & C_{12} & 0 & 0 & 0\\
C_{12} & C_{11} & C_{12} & 0 & 0 & 0\\
C_{12} & C_{12} & C_{11} & 0 & 0 & 0\\
0 & 0 & 0 & C_{44} & 0 & 0\\
0 & 0 & 0 & 0 & C_{44} & 0\\
0 & 0 & 0 & 0 & 0 & C_{44}\end{array}\right]
\end{aligned}$$

## Effect of crystal symmetries (II)

Less symmetric crystals have, naturally, a higher number of independent
elastic constants and lower symmetry of the $C_{ij}$ matrix:

* cubic - 3
* hexagonal - 5
* rombohedral - 6
* tetragonal - 6
* rombic - 9
* monoclinic - 12
* triclinic - 18

## Numerical derivation of elastic matrix

Numerical derivation of the $C_{ij}$ matrix may be approached in many
different ways. Basically, we can employ the same methods as used
effectively in experimental work. From all experimental procedures we
can select three classes which are relevant to our discussion:

1.  Based on the measured sound velocity:
$$
\varrho v_{k}^{2}=L(C_{ij})
$$
where $L(C_{ij})$ is a linear combination of independent components of elastic tensor, $v_{k}$ is a long-wave sound velocity in particular direction, and $\varrho$ is crystal density. 
    
2.  Based on the strain-energy relation: non-linear, impractical or impossible in experiment.

3.  Based on the measured stress-strain relations for simple strains: linear relation, possible in the laboratory, well-conditioned numerically.

## Small displacement method (I)

![](deform_black.png){width="66%" fig-align="center"}

Starting from set of calculated stresses and strains$\{u^{a}, \sigma^{a}\}$:

$$
\{u^{a}, \sigma^{a}\} \rightarrow C_{ij}u_{j}^{a}=\sigma_{i}^{a} \rightarrow 
S_{j\mu}(u^{a})C_{\mu}=\sigma_{j}^{a}
$$

$\mu$ - numbers independent components of $C_{ij}$

$S(u)$ linear function of the strain vector $u$ with all symmetry
relations taken into account. 

The set of necessary deformations can be determined by the
symmetry of the crystal and contains tetragonal and sheer deformations
along selected or all axis - as the symmetry of the case dictates. To
improve the accuracy of the results the deformations may be of different
sizes (typically 0.1-1% in length or 0.1-1 degree in angle).

## Small displacement method (II)

For cubic lattice:

$$\begin{aligned}
\left[\begin{array}{ccc}
u_{1} & u_{2}+u_{3} & 0\\
u_{2} & u_{1}+u_{3} & 0\\
u_{3} & u_{1}+u_{2} & 0\\
0 & 0 & 2u_{4}\\
0 & 0 & 2u_{5}\\
0 & 0 & 2u_{6}\end{array}\right]^{a}\left[\begin{array}{c}
C_{11}\\
C_{12}\\
C_{44}\end{array}\right]=\left[\begin{array}{c}
\sigma_{1}\\
\sigma_{2}\\
\sigma_{3}\\
\sigma_{4}\\
\sigma_{5}\\
\sigma_{6}\end{array}\right]^{a}.
\end{aligned}$$

The elements of the S matrix are simply coefficients of first
derivatives of the F(u) over respective strain components.
Alternatively, we can rewrite the S(u) matrix in the compact form as a
mixed derivative:

$$S_{i\mu}=A\frac{\partial^{2}F}{\partial u_{i}\partial C_{\mu}},$$

where A is a multiplier taking into account the double counting of the
off-diagonal components in the free energy formula. The multiplier $A=1$ for $i \leq 4$,
and $1/2$ otherwise.

## Small displacement method (III)

For example, in the orthorhombic crystal the vector of independent
$C_{ij}$ components has nine elements and the S matrix is a $9\times6$
one:
$$\begin{aligned}
\left[\begin{array}{ccccccccc}
u_{1} & 0 & 0 & u_{2} & u_{3} & 0 & 0 & 0 & 0\\
0 & u_{2} & 0 & u_{1} & 0 & u_{3} & 0 & 0 & 0\\
0 & 0 & u_{3} & 0 & u_{1} & u_{2} & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 2u_{4} & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 2u_{5} & 0\\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 2u_{6}\end{array}\right]^{a}\left[\begin{array}{c}
C_{11}\\
C_{22}\\
C_{33}\\
C_{12}\\
C_{13}\\
C_{23}\\
C_{44}\\
C_{55}\\
C_{66}\end{array}\right]=\left[\begin{array}{c}
\sigma_{1}\\
\sigma_{2}\\
\sigma_{3}\\
\sigma_{4}\\
\sigma_{5}\\
\sigma_{6}\end{array}\right]^{a}.
\end{aligned}$$

comes from the free energy formula:

$$\begin{aligned}
F(u)   =  \frac{1}{2}C_{11}u_{1}^{2}+
\frac{1}{2}C_{22}u_{2}^{2}+
\frac{1}{2}C_{33}u_{3}^{2}+ 
C_{12}u_{1}u_{2}+C_{13}u_{1}u_{3}+C_{23}u_{2}u_{3}+ \\
2C_{44}u_{4}^{2}+2C_{55}u_{5}^{2}+2C_{66}u_{6}^{2}
\end{aligned}$$

## Small displacement method (IV)

The above general formula turns out to be quite helpful in less trivial cases of trigonal or hexagonal classes. For instance, rather long hexagonal elastic free energy (see L&L) leads to the following set of equations:

$$\begin{aligned}
\left[\begin{array}{ccccc}
u_{1} & 0 & u_{2} & u_{3} & 0\\
u_{2} & 0 & u_{1} & u_{3} & 0\\
0 & u_{3} & 0 & u_{1}+u_{2} & 0\\
0 & 0 & 0 & 0 & 2u_{4}\\
0 & 0 & 0 & 0 & 2u_{5}\\
u_{6} & 0 & -u_{6} & 0 & 0\end{array}\right]^{a}\left[\begin{array}{c}
C_{11}\\
C_{33}\\
C_{12}\\
C_{13}\\
C_{44}\end{array}\right]=\left[\begin{array}{c}
\sigma_{1}\\
\sigma_{2}\\
\sigma_{3}\\
\sigma_{4}\\
\sigma_{5}\\
\sigma_{6}\end{array}\right]^{a}.
\end{aligned}$$

The set of equations is usually over-determined. Therefore, it cannot be solved in the strict linear-algebra sense since no exact solution could exist. The approximate solution may be fitted to the equation using Singular Value Decomposition (SVD). This method provides the approximate solution minimising the residual vector of the equation but also is stable against numerically ill-conditioned equations or equations which provide too little data to determine all components of the solution.

## Calculation procedure

![](../images/flow.pdf){width="80%" fig-align="center"}