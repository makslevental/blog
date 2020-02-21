---
layout: post
title: Risk Neutral Measures
published: true
---

This post makes rigorous the material in the previous two posts ([Change of Measure]({% post_url 2020-02-17-Change-of-Measure %})
and [Girsanov Theorem]({% post_url 2020-02-19-Girsanov-Theorem %}) 
) in the context of asset pricing.

# Radon-Nikodym

**Definition**: Two probability measure $P,Q$ are said to be **equivalent** if they pick the same measure-zero sets, i.e. $P(A) \iff Q(A)$.

**Example**: Let $Z$ be a random variable (rv) against measure $P$ such that $E^P[Z] = 1$ and $Z>0$. Then 

$$
	Q(A) = E^P[Z\, 1_A] = \int\limits_A Z dP
$$

for all events $A$. Then $Q$ is equivalent to $P$. The assumption that $E^P[Z] = 1$ is required to guarantee $Q(\Omega) = 1$; if only $E^P[Z] < \infty$ then we could normalize $Z$ in the integral and still handily define the measure $Q$.

**Definition**: When $Q$ is defined as such then we write 

$$
	dQ := ZdP \quad \text{or} \quad \frac{dQ}{dP} := Z
$$

and we say that $Z$ is the **density** of $Q$ w.r.t. $P$.

**Theorem**: (Radon-Nikodym) Two measures $Q,P$ are equivalent iff there exists a random variable $Z$ such that $E^P[Z] = 1$ and $Q$ is defined as above. $Q$ is called the **Radon-Nikodym** derivative of $Q$ w.r.t. $P$.

# Martingales

Martingales are stochastic processes that are "fair".

**Definition**: Let $(\Omega, \mathscr{F}, P)$ be a probability space and let $I$ be a totally ordered index set (usually $\mathbb{R}^+$ or $\mathbb{N}$). 
Also for every $i \in I$ let $\mathscr{F}_i$ be a sub-$\sigma$-algebra of $\mathscr{F}$.
Then the sequence $(\mathscr{F}_i)$ is called a **filtration**, if 

$$
	\mathscr{F}_k \subseteq \mathscr{F}_\ell \subseteq \mathscr{F}
$$

for all $k \leq \ell$. 
In short, filtrations are families of monotonic (in terms of inclusion) $\sigma$-algebras.
If $(\mathscr{F}_i)$ is a filtration then $\left( \Omega, \mathscr{F},(\mathscr{F}_i), P \right)$ is called a **filtered probability space**.

**Definition**: A stochastsic process $Z: T \times \Omega \rightarrow S$ is a **Martingale** w.r.t. a filtration $\mathscr{F}_t$ and probability measure $P$ if

1. $Z_t$ is *adapted* to the filtration, i.e. for each $t$ in the index set $T$, $Z_t$ is $\mathscr{F}_t$-measurable.
2. $Z_t \in L^1$, i.e. 

	$$ 
	E^P[|Z_t|] < \infty 
	$$

3. For all $s < t$  

	$$ 
	\begin{aligned}
	E^P[Z_t - Z_s &| \mathscr{F}_s] = 0 \\
	&\iff \\
	E^P[Z_t &| \mathscr{F}_s] = Z_s \\
	\end{aligned}
	$$

Suppose $T>0$ is fixed and $Z$ is a Martingale.
Define

$$
	dQ = Z_T dP
$$

and $X$ a rv.
Then

$$
	E^Q [X] := E^P[Z_T X] = \int Z_T X dP
$$

Similarly conditional expectation 
$E^Q [X | \mathscr{F}]$ 
(conditioned on some $\mathscr{F}$ and for some event $F \in \mathscr{F}$) is defined as the unique rv such that

$$
	\int_F E^Q [X | \mathscr{F}] dQ = \int_F X dQ
$$

**Theorem**: (Cameron-Martin-Girsanov) Let $B_t$ be a Brownian motion under some measure $P$ and let $\mu_t$ be adapted to same filtration as $B_t$ (so that they're jointly $\mathscr{F}_t$-measurable).
Define 

$$
	\tilde{B}_t := B_t - \int_0^t \mu_s ds
$$

and 

$$
	Z_t := e^{\int_0^t \mu_t dB - \frac{1}{2}\int_0^t \mu_s^2 ds}
$$

and 

$$
	dQ = Z_T dP
$$

If $Z_t$ is a Martingale under $P$ then $\tilde{B}_t$ is a Brownian motion under $Q$ (up to time $T$).

Note that $P(Z_0 = 0) = 1$ and if $Z_t$ is a Martingale then $E^P[Z_T] = 1$, thereby ensuring that $Q$ is a probability measure (the 1 "propagates").
The Martingale requirement is a hard constraint. 
In general $Z_t$ is a super-Martingale and so $E^P[Z_T] \leq 1$ (which foils $Q$ being a finite probability measure). 
Two conditions that guarantee that $Z$ is a Martingale are the **Novikov** and **Kazamaki** conditions

$$
	E^P[e^{\frac{1}{2}\int_0^t \mu_s^2 ds}] < \infty \quad \text{or} \quad E^P[e^{\frac{1}{2}\int_0^t \mu_s dB}] < \infty
$$

but these often do not apply and proving that $Z_t$ is Martingale is required.

