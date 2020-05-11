---
layout: post
title: Connections
published: true
---

# Tangent vectors
The most general definition of a vector tangent to a manifold involves *derivations*.
$$
\newcommand{\R}{\mathbb{R}}
\newcommand{\vec}{\mathbf}
\newcommand{\parens}[1]{\left(#1 \right)}
\newcommand{\braces}[1]{\left\{#1 \right\}}
\newcommand{\angles}[1]{\langle #1 \rangle}
\newcommand{\d}{\text{d}}
\newcommand{\dd}[1]{\frac{\d}{\d #1}}
\newcommand{\ddd}[2]{\frac{\d #1}{\d #2}}
\newcommand{\pd}[1]{\frac{\partial}{\partial #1}}
\newcommand{\p}{\partial}
\newcommand{\pdd}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\evalat}[1]{\Big|_{#1}}
$$

Let $M$ be a smooth manifold; every point $p \in M$ has a neighborhood $U \subset M$ that can be mapped smoothly[^1] to $\R^n$ for some $n$ (the dimension of the manifold). 
**Therefore each $p$ can be identified with its coordinates**[^2] $\phi(p) = \parens{x^1(p), \dots, x^n(p)}$.

Associated with each point is the *tangent space* $T_p M$. 
Elements of the tangent space are called *tangent vectors* and can be intuitively visualized as arrows tangent to the point; this can be made rigorous by way of *directional derivatives*.
Let $c(t) = \parens{p^1 +t v^1, \dots, p^n +t v^n}$ be a parameterization of a line through the point $p$ in the direction of $\vec{v}$; if $f \in C^{\infty}_p$ in a neighborhood of $p$ then the directional derivative of $f$ in the direction of $\vec{v}$ is defined

$$
    D_{\vec{v}} f := \lim_{t\rightarrow 0} \frac{f(c(t)) -f(p)}{t} = \dd{t} f(c(t)) \Big|_{t=0}
$$

By the chain rule

$$
    \begin{aligned}
        D_{\vec{v}} f &= \sum_{i=1}^{n} \pdd{f}{x^i} \Big|_p \ddd{c^i}{t} \Big|_{t=0} \\
        &=  \sum_{i=1}^{n} \ddd{c^i}{t} \Big|_{t=0} \pdd{f}{x^i} \Big|_p \\
        &=  \sum_{i=1}^{n} v^i \pdd{f}{x^i} \Big|_p
    \end{aligned}
$$

and hence the directional derivative in the direction of $\vec{v}$ is defined

$$
    D_{\vec{v}} := \sum_{i=1}^{n} v^i \pdd{}{x^i} \Big|_p
$$

This directional derivative gives a map between between vector spaces

$$
    D_{\vec{v}}: C^{\infty}_p \rightarrow \R
$$

that also satisfies the *Leibniz rule*

$$
    D_{\vec{v}}(f g) = (D_{\vec{v}}f) g + f (D_{\vec{v}}g)
$$

In general any linear map from $C^{\infty}_p \rightarrow \R$ is called a *derivation* and the set of all derivations is a vector space[^3].
So we can identify tangent vectors[^4] with a legitimate vector space spanned by the basis

$$
    \braces{\p_1, \dots, \p_n} := \braces{\pd{x^1} \evalat{p}, \dots, \pd{x^n} \evalat{p}}
$$

The point being that, while not as geometrically intuitive
as arrows, this generalizes to manifolds.

Alternative notiation for directional derivative

$$
\vec{v}(f) := D_{\vec{v}} f
$$

# Covariant derivatives

Invariably (pardon the pun) when doing physics you'll need derivatives of quantities. This prompts the question: how do you differentiate a vector field[^5]?
Suppose we have a vector field $\vec{w}(p) = \parens{w^i(p)}$ that varies smoothly with $p$.
Notice that each $w_i: M \rightarrow \R$ is a smooth function so it can be differentiated in a straightforward fashion: 


$$
\vec{v}(w^i) = D_{\vec{v}} w^i
$$

Collecting all of these into a column we get 

$$
\vec{v}(w) = \begin{bmatrix}
     D_{\vec{v}} w^1 \\
     \vdots \\
     D_{\vec{v}} w^n
    \end{bmatrix} = {\frac {\partial (w^{1},..,w^{n})}{\partial (x^{1},..,x^{n})}} \vec{v} = \vec{J} \vec{v}
$$

where $\vec{J}$ is the Jacobian of $\vec{w}(p)$. 
Alternatively in components

$$
    (vw)^i = v w^i = \sum_j v^j \p_j w^i
$$

Unfortuntely this doesn't generalize so we define abstract differentiation of one vector field with respect to another.
Define $TM := \bigsqcup_{p \in M}$ as the *tangent bundle* of $M$; an element of the tangent bundle is of the form $(p, \vec{v})$ with $p \in M$ and $\vec{v} \in T_p M$.
In fact $TM$ has a smooth manifold structure[^6]; let $\pi: TM \rightarrow M$ be the bundle projection.
A *section* of $TM$ is a map $F:M \rightarrow TM$ is an assignment of a vector to every $p \in M$, i.e. vector field on $M$. Thus, a vector field is smooth if the section $F$ is a smooth map between manifolds.

Let $\mathcal{T}(M)$ denote the space of smooth sections of $TM$, i.e. the space of smooth vector fields on $M$, and define a *connection* $\nabla: \mathcal{T}(M) \times \mathcal{T}(M) \rightarrow \mathcal{T}(M)$ on $M$.
Written $(\vec{v},\vec{w}) \mapsto \nabla_{\vec{v}} \vec{w}$, the connection satisfies

1. $\nabla_{\vec{v}} \vec{w}$ is linear in $\vec{v}$ over $f,g \in C^{\infty}(M)$:

   $$
        \nabla_{f \vec{v}_1 + g \vec{v}_2} \vec{w} = f \nabla_{\vec{v}_1} \vec{w} + g \nabla_{\vec{v}_2} \vec{w}
   $$
2. $\nabla_{\vec{v}} \vec{w}$ is linear in $\vec{w}$ over $a,b \in \R$:

   $$
        \nabla_{\vec{v}} \parens{a \vec{w}_1 + b \vec{w}_2} = a \nabla_{\vec{v}}\vec{w}_1 + b \nabla_{\vec{v}}\vec{w}_2
   $$
3. For all $f \in C^{\infty}(M)$ the connection satisfies a product rule

   $$
        \nabla_{\vec{v}} \parens{f \vec{w}} = f \nabla_{\vec{v}} \vec{w} + (vf)\vec{w}
   $$

$\nabla_{\vec{v}} \vec{w}$ is also called the *covariant derivative* of $\vec{w}$ in the direction $\vec{v}$.

<!-- each element of the tangent space is the equivalence of class of curves through $p$ that agree on a neighborhood containing $p$ and  -->


# Foonotes


[^1]: A topological space $M$ is *locally Euclidean of dimension $n$*  if for every $p \in M$ there exists a neighborhood $U$ such that there is a $homeomorphism$ $\phi$ from $U$ **onto** an opensubset of $\mathbb{R}^n$. The pair $\left( U,\phi \colon U \rightarrow \R^n \right)$ is called a *chart*, with *U* being the *coordinate neighborhood* and $\phi$ the *coordinate system*.

[^2]: The sense here is akin to latitude and longitude coordinates on the earth: coordinates are a mapping from the spherical earth (a manifold $S^2$) to a rectilinear coordinate system $\R^2$.

[^3]: Loring Tu's An Introduction to Manifolds: Theorem 2.2.

[^4]: Tangent vectors $\iff$ directional derivatives $\iff$ derivations.

[^5]: The assignment of a vector from $T_p M$ to each $p \in M$.

[^6]: A *vector bundle* is a family of vector spaces parameterized by another space. A vector bundle consists of a *base space* $X$, a *total space* $E$, a continuous surjection (called the bundle projection) $\pi: E \rightarrow X$, and where for every $x \in X$ the *fiber* $\pi^{-1}(x)$ is a finite-dimensional vector space.

<!-- [^1]: Assume a general, linear, second-order PDE in two variables $u(x,y)$

    $$
        Au_{xx}+2Bu_{xy}+Cu_{yy}+\cdots {\mbox{(lower order terms)}}=0,
    $$
    This form of the PDE resembles a conic section and naturally suggests a classification based on the value of the discriminant
    * $B^2 - A C < 0$: elliptic partial differential equation
    * $B^2 - A C = 0$: parabolic partial differential equation
    * $B^2 - A C > 0$: hyperbolic partial differential equation -->

<!-- [^2]: A good mnemonic is "low-co-row".
  
[^3]: Einstein summation convetion.

[^4]: A map from the vector space to the ground field that's linear in both of its arguments.

[^5]: Actually it's vector spaces; The *tensor product* $V \otimes W$ of two vector spaces $V$ and $W$ (over the same field) is itself a vector space, endowed with the operation of bilinear composition, denoted by $\otimes$, from ordered pairs in the Cartesian product $V \times W$ to $V \otimes W$ in a way that generalizes the outer product (quotienting). -->
