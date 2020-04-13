---
layout: post
title: Einstein Field Equations
published: false
---
$$\newcommand{\vec}{\mathbf}$$

In general theory of relativity (GR) the *Einstein field equations* relate the geometry of space-time with the distribution of matter within it.

# Introduction

Einstein's field equations describe the curvature of space as a function of energy and momentum; they're a system of ten coupled, nonlinear, hyperbolic-elliptic partial differential equations[^1]. 
Typically the equations are expressed in tensor form as 

$$
    {\displaystyle R_{\mu \nu }-{\tfrac {1}{2}}Rg_{\mu \nu }+\Lambda g_{\mu \nu }={\frac {8\pi G}{c^{4}}}T_{\mu \nu }}
$$

where $R_{\mu \nu }$ is the Ricci curvature tensor, $R$ is the scalar curvature, $g_{\mu \nu }$ is the metric tensor, $\Lambda$ is the cosmological constant, $G$ is Newton's gravitational constant, $c$ is the speed of light in vacuum, and $T_{\mu \nu }$ is the stress–energy tensor. Each covariant (explained in the forthcoming) index $\mu, \nu$ can take on values $0,1,2,3$ thereby giving 16 different equations in principle, but it turns out each of the tensors is symmetric thereby reducing the number of unique equations to ten.

# Tensors

## Change of basis

Suppose we have two orthonormal bases $(\vec{u}_1, \vec{u}_2)$, $(\vec{v}_1, \vec{v}_2)$ related to each other by a rotation $\theta$

<p>
<img style="display:block; margin:auto;" src="{{ "/images/einstein/basis.png" | absolute_url }}">
</p>

It's clear that 

$$
    \begin{align*}
        \vec{v}_1 &= \vec{u}_1 \cos\theta + \vec{u}_2 \sin\theta, \\
        \vec{v}_2 &= \vec{u}_1 (-\sin\theta) + \vec{u}_2 \cos\theta.
    \end{align*} 
$$

Note that both $\vec{v}_1, \vec{v}_2$ have unit length. 
Alternatively 

$$
    \begin{align*}
        (\vec{v}_1, \vec{v}_2) &= (\vec{u}_1, \vec{u}_2)
            \begin{pmatrix}
                \cos\theta & -\sin\theta \\
                \sin\theta & \cos\theta
            \end{pmatrix} \\
            &= (\vec{u}_1, \vec{u}_2)R\left(\theta\right)
    \end{align*}
$$

where $R(\theta)$ is the rotation matrix. 
Now suppose we have a vector $\vec{x}$ defined in the $(\vec{u}_1, \vec{u}_2)$ basis

$$
        \vec{x} = \left(\vec{u}_1, \vec{u}_2\right)
            \begin{pmatrix}
                x_1 \\ x_2
            \end{pmatrix}
$$

and in the $(\vec{v}_1, \vec{v}_2)$ basis

$$
        \vec{x} = (\vec{v}_1, \vec{v}_2)
            \begin{pmatrix}
                x'_1 \\ x'_2
            \end{pmatrix}
$$


<p>
<img style="display:block; margin:auto;" src="{{ "/images/einstein/basis-change.png" | absolute_url }}">
</p>

Equating both expressions for $\vec{x}$ 

$$
    (\vec{u}_1, \vec{u}_2)
        \begin{pmatrix}
            x_1 \\ x_2
        \end{pmatrix} =
(\vec{v}_1, \vec{v}_2)
            \begin{pmatrix}
                x'_1 \\ x'_2
            \end{pmatrix} = (\vec{u}_1, \vec{u}_2)R\left(\theta\right)\begin{pmatrix}
                x'_1 \\ x'_2
            \end{pmatrix}
$$

we get that the relationship between the scalar components is

$$
        \begin{pmatrix}
            x_1 \\ x_2
        \end{pmatrix} =
             R\left(\theta\right)\begin{pmatrix}
                x'_1 \\ x'_2
            \end{pmatrix}
$$

Because $R(\theta) \in \text{SO}(2)$[^3] (or just by verification)

$$
    R(\theta)^t = R(\theta)^{-1} = R(-\theta)
$$

Therefore we can write

$$
\begin{pmatrix}
                x'_1 \\ x'_2
            \end{pmatrix} = R(\theta)^{-1} \begin{pmatrix}
                x_1 \\ x_2
            \end{pmatrix} = R(-\theta) \begin{pmatrix}
                x_1 \\ x_2
            \end{pmatrix}
$$

which can be summarized as: **rotating a basis by an angle $\theta$ is equivalent to rotating all vectors by the angle $-\theta$**.

## Co/contravariance and index notation

We can express the change of basis equation using index notation and the Einstein summation convention[^4]

$$
    \vec{v}_i = \sum_{j=1}^2 \vec{u}_j R_i^j = \vec{u}_j R_i^j
$$

This transformation describes the new basis vectors as a linear combination of the old basis vectors,
where $R_i^j$ is the entry in the rotation matrix $R(\theta)$ in the $i$th column and $j$th row[^2].
Such a transformation is *defined* to be a **covariant transformation** and any other quantity transforms in the same way (i.e. according to the "forward" direction of the change of basis) also called **covariant**.

Using this notation we can also reiterate the vector transformation law as

$$
    x'^i = (R^{-1})_j^i x^j
$$

where $(R^{-1})_j^i$ is the entry in the $j$th column and $i$th row of the inverse rotation matrix $R(\theta)^{-1}$.
Any quantity that transforms in such a way (i.e. according to the inverse of the change of basis) is called **contravariant**.

The intuition here is that if a vector represents a physical or geomtrical quantity (having the same magnitude and direction after a change of basis) then its *components* must transform contravariantly (in a sense "compensating" for the effect of the change of basis).

# Foonotes

[^1]: Assume a general, linear, second-order PDE in two variables $u(x,y)$

    $$
        Au_{xx}+2Bu_{xy}+Cu_{yy}+\cdots {\mbox{(lower order terms)}}=0,
    $$
    This form of the PDE resembles a conic section and naturally suggests a classification based on the value of the discriminant
    * $B^2 - A C < 0$: elliptic partial differential equation
    * $B^2 - A C = 0$: parabolic partial differential equation
    * $B^2 - A C > 0$: hyperbolic partial differential equation

[^2]: A good mnemonic is "low-co-row": 

    * since the prototypical covariant object is a basis, i.e. a "row" of vectors, and basis vectors are denoted by lower indices, in general components of covariant objects have lower indices.
    * since the prototypical contravariant object is a vector, i.e. a column of scalar quantities, in general components of contravariant objects have upper indices.
  
[^3]: Special orthogonal group of dimension two.
[^4]: Repeated indices are summed over.