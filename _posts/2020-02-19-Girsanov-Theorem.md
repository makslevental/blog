---
layout: post
title: Girsanov Theorem
published: true
---

# Change of measure of a finite dimensional Stochastic Process

This post follows [this video](https://www.youtube.com/watch?v=vKjbau2Hlrs). 

Consider a collection Normal random variables 

$$
	X_0, X_1, X_2, \dots, X_n
$$

where the indices can be taken to correspond with discrete times

$$
	t_0 < t_1 < t_2 < \cdots < t_n
$$

This is a finite dimensional stochastic process.
Assume that $P(X_0 = 0) = 1$ and that increments $\Delta X_i := X_{i+1} - X_i$ are distributed Normal

$$
	\Delta X_i \sim N(0, \Delta t_i)
$$

where $\Delta t_i := t_{i+1} - t_i$.

A mechanical procedure for generating $X_i$ is to start at zero, draw an increment some time $\Delta t$ later, add it to the previous total sum, and repeat.
Here's what several such trajectories (*sample paths*) look like

![]({{ "/images/brownian.png" | absolute_url }})

The unconditional distribution for $X_n$ is

$$
	X_n := \sum_{i=1}^n \Delta X_i \sim N\left(0, t_n\right)
$$

The conditional distribution of $X_i$ given $X_{i-1}$, i.e. given its previous value, is

$$
\begin{align}
	X_i | (X_{i-1} = x_{i-1}) &\sim N(x_{i-1}, \Delta t) \\
	& \iff \\
	p(x_i - x_{i-1} | x_{i-1}) &= \frac{1}{\sqrt{2\pi \Delta t}} e^ { -\frac{1}{2\Delta t} \left( x_i - x_{i-1} \right)^2 }
\end{align}
$$

We now ask what the probability of the event $A$ that each of the $X_i$ being within a range, i.e. 

$$
	P(A) = P\left( \alpha_1 \leq X_1 \leq \beta_1, \alpha_2 \leq X_2 \leq \beta_2,\dots,\alpha_n \leq X_n \leq \beta_n \right)
$$

Since the conditional distributions are independent we can write this as 

$$
\begin{align}
	P(A) &= \int\limits_{\alpha_1}^{\beta_1}\int\limits_{\alpha_2}^{\beta_2}\cdots\int\limits_{\alpha_n}^{\beta_n} p(x_1) p(x_2 - x_1 | x_1) \cdots p(x_n - x_{n-1} | x_{n-1}) dx_1 dx_2 \cdots dx_n \\
	&= \frac{1}{(2\pi \Delta t)^{n/2}}\int\limits_{\alpha_1}^{\beta_1}\int\limits_{\alpha_2}^{\beta_2}\cdots\int\limits_{\alpha_n}^{\beta_n} e^ { -\frac{1}{2\Delta t} \sum_{i=1}^{n} (x_i - x_{i-1})^2} dx_1 dx_2 \cdots dx_n
\end{align}
$$

Now we change the measure on each random variable by shifting the interval

$$
	P\left(\alpha_1 -\mu_1 \Delta t \leq X_1 \leq \beta_1 - \mu_1 \Delta t, \dots, \alpha_n -\sum_{i=1}^n \mu_i \Delta t \leq X_n \leq \beta -\sum_{i=1}^n \mu_i \Delta t\right)
$$

Making the substitution into the integral

$$
\begin{align}
	P(A-\mu) &= \int\limits_{ \alpha_1 -\mu_1 \Delta t}^{\beta_1 -\mu_1 \Delta t}\cdots\int\limits_{ \alpha_n -\sum_{i=1}^n \mu_i \Delta t}^{\beta_n -\sum_{i=1}^n\mu_i \Delta t} p(x_1)  \cdots p(x_n - x_{n-1} | x_{n-1}) dx_1 dx_2 \cdots dx_n 
\end{align}
$$

Making the change of variables to restore the original limits of integration is similar to the 1D case. 
We demonstrate for the $n=2$ case

$$
\begin{align}
&=\frac{1}{2\pi \Delta t} \int\limits_{ \alpha_1 -\mu_1 \Delta t}^{\beta_1 -\mu_1 \Delta t}\int\limits_{ \alpha_2 - (\mu_1 + \mu_2)\Delta t}^{ \beta_2 - (\mu_1 + \mu_2)\Delta t} e^ { -\frac{1}{2\Delta t} (x_1-x_0)^2} e^{-\frac{1}{2\Delta t}(x_2-x_1)^2 } dx_1 dx_2 
\end{align}
$$

Then $y_1 = x_1 + \mu_1 \Delta t$ implies

$$
\begin{align}
&=\frac{1}{2\pi \Delta t} \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 - (\mu_1 + \mu_2)\Delta t}^{ \beta_2 - (\mu_1 + \mu_2)\Delta t} e^{ -\frac{1}{2\Delta t} (y_1-x_0-\mu_1 \Delta t)^2}e^{ -\frac{1}{2\Delta t}(x_2-y_1+\mu_1\Delta t)^2 } dy_1 dx_2 
\end{align}
$$

and $y_2 = x_2 + (\mu_1 + \mu_2) \Delta t$ implies

$$
\begin{align}
&=\frac{1}{2\pi \Delta t} \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta_2 } e^{ -\frac{1}{2\Delta t} (y_1-x_0-\mu_1 \Delta t)^2 } e^{ -\frac{1}{2\Delta t}(y_2-(\mu_1+\mu_2)\Delta t-y_1+\mu_1\Delta t)^2 } dy_1 dy_2 \\
&=\frac{1}{2\pi \Delta t} \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta_2 } e^{ -\frac{1}{2\Delta t} (y_1-x_0-\mu_1 \Delta t)^2 } e^{ -\frac{1}{2\Delta t}(y_2-y_1-\mu_2 \Delta t)^2} dy_1 dy_2 
\end{align}
$$

Then changing the dummy variable $y_i \rightarrow x_i$

$$
\begin{align}
&=\frac{1}{2\pi \Delta t} \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta_2 } e^{ -\frac{1}{2\Delta t} (x_1-x_0-\mu_1 \Delta t)^2 } e^{ -\frac{1}{2\Delta t}(x_2-x_1-\mu_2 \Delta t)^2 } dx_1 dx_2  \\
&=\frac{1}{2\pi \Delta t} \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta_2 } e^{ -\frac{1}{2\Delta t} \left(\sum_{i=1}^2 x_i - x_{i-1} -\mu_i \Delta t\right)^2} dx_1 dx_2

\end{align}
$$

Generalizing to $n$ time steps we get 

$$
\begin{align}
P(A-\mu) &= \frac{1}{(2\pi \Delta t)^{n/2}} \int\limits_{ \alpha_1 }^{\beta_1 }\cdots\int\limits_{ \alpha_n }^{ \beta_n } e^{ -\frac{1}{2\Delta t} \left(\sum_{i=1}^n x_i - x_{i-1} -\mu_i \Delta t\right)^2} dx_1 \cdots dx_n
\end{align}
$$

Now expanding the square and splitting the exponential

$$
\begin{align}
P(A-\mu) &= \frac{1}{(2\pi \Delta t)^{n/2}} \int\limits_{ \alpha_1 }^{\beta_1 }\cdots\int\limits_{ \alpha_n }^{ \beta_n } e^{ -\frac{1}{2\Delta t} \left(\sum_{i=1}^n \Delta x_i \right)^2}e^{  \sum_{i=1}^n \mu_i \Delta x_i -\frac{1}{2}\mu_i^2 \Delta t} dx_1 \cdots dx_n
\end{align}
$$

Defining

$$
	Z_n =  e^{  \sum_{i=1}^n \mu_i \Delta X_i -\frac{1}{2}\mu_i^2 \Delta t}
$$

we have just as in the single variable case

$$
\begin{align}
	P(A-\mu) &= \int\limits_A z_n dP(x) \\
	&= Q(A) \\ 
	\frac{dQ}{dP} &= z_n \\
	E^Q \left[ h(X) \right] &= E^P \left[ Z(X) h(X) \right]
	
\end{align}
$$

Under this new measure $Q$

$$
	X_n \sim N \left(\sum_{i=1}^n \mu_i \Delta t, t_n \right)
$$

Note the difference w.r.t. the distribution of $X_n$ under the original measure $P$
i.e. $X_n$ under the new measure is mean shifted by $\sum_{i=1}^n \mu_i \Delta t$. 
It follows that under the new measure $Q$

$$
	X_n - \sum_{i=1}^n \mu_i \Delta t \sim N\left(0, t_n\right)
$$

What's happening here is that the process is being centering by the change of measure

![]({{ "/images/Girsanov.png" | absolute_url }})

# Girsanov Theorem

If we squint at 

$$
	Z_n =  e^{  \sum_{i=1}^n \mu_i \Delta X_i -\frac{1}{2}\mu_i^2 \Delta t}
$$

the sum in the exponential looks like the sum approximation to the Ito integral

$$
	\int\limits_0^t \mu_s dB - \frac{1}{2} \int\limits_0^t \mu_s^2 ds
$$

where in the limit as $\Delta t \rightarrow 0$ the process $X_i$ becomes a continuous-time Brownian motion $B_t$.
The Girsanov theorem states that if $B_t$ is a Brownian motion under a measure $P$ then shifting the intervals of integration by 

$$
	\int\limits_0^t \mu_s ds
$$

produces another measure $Q$ with Radon-Nikodym *process* $Z_t$

$$
	Z_t := \frac{dQ}{dP} = e^{ \int_0^t \mu_s dB_s - \frac{1}{2} \int_0^t \mu_s^2 ds }
$$

**and** under this new measure $Q$

$$
	\tilde{B}_t := B_t - \int\limits_0^t \mu_s ds 
$$

is a Brownian motion.

If the shifts $\mu_i$ don't depend on time then the relations simplify to 

$$
	Z_t := \frac{dQ}{dP} = e^{\mu B_s - \frac{1}{2}  \mu_s^2 t}
$$

and

$$
	\tilde{B}_t := B_t - \mu t
$$

We prove Girsanov's theorem in this simplified case.

## Martingale

We have to show that $Z_t$ is a valid density in continuous time. 
This is equivalent to showing that its expectation under the measure $P$ is equal to 1 or alternatively that it is Martingale

$$
	E^P \left[ Z_t | \mathscr{F}_s \right] = Z_s
$$

where $\mathscr{F}_s$ is a filtration to which $Z_t$ is adapted (i.e. $Z_t$ is $\mathscr{F}_t$-measurable for all $t \geq 0$).
Assuming that the process is bounded we only need to show that it is local Martingale to show that it is Martingale. 
One way to do this to show that it is an Ito diffusion with no drift term (**TODO**).
To do this we apply Ito's lemma to the exponential.
Let $X = \mu B_t - \frac{1}{2} \mu^2 t$ and then

$$
\begin{align}
	Z_t &= e^{ \mu B_t - \frac{1}{2}  \mu_s^2 t } \\
	&= e^X
\end{align}
$$

Recall that the Ito differential of an exponential is (**TODO**)

$$
	dZ_t = e^X \left(dX + \frac{1}{2}dX^2 \right)
$$

Therefore we need to calculate $dX$ and $dX^2$.
Since $\mu$ is constant we have that $dX = \mu dB - \frac{1}{2}\mu^2 dt$ and $dX^2 = \mu^2 dt$ (**TODO**).
Substituting these into $dZ_t$ we get

$$
\begin{align}
	dZ_t &= Z_t \left( \mu dB -\frac{1}{2}\mu^2 dt + \frac{1}{2}\mu^2 dt \right) \\
	&= \mu Z_t dB
\end{align}
$$

and so we see that there is no drift term and hence $Z_t$ is a local Martingale.
To compute the expectation

$$
	E^P \left[ Z_t | \mathscr{F}_s \right] = E \left[ e^X \right]
$$

we note that 

$$

X = \mu B_t - \frac{1}{2}\mu t \sim N\left(-\frac{1}{2}\mu^2 t, \mu^2 t \right)

$$

is a Brownian motion and so $e^X$ is a geometric Brownian motion with expectation (**TODO**)

$$
\begin{align}
	E \left[ e^X \right] &= e^{E[X] + \frac{1}{2} \text{Var}[X } \\
	&= e^{ -\frac{1}{2}\mu^2 t + \frac{1}{2}\mu^2 t } \\
	&= 1
\end{align}
$$

Hence $Z_t$ is a valid density process.

## Brownian Motion

We need to show that 

$$
	\tilde{B}_t = B_t - \int\limits_0^t \mu_s ds 
$$

is a Brownian motion under the measure $Q$.
The standard definition of a Brownian motion is


1. $P(\tilde{B}_0 = 0) = 1 $
2. Independent increments $\Delta \tilde{B} := \tilde{B}_t - \tilde{B}_s$
3. $\Delta \tilde{B} \sim N (0, t-s)$


An alternative definition (Levi's characterization) is 

1. $P(\tilde{B}_0 = 0) = 1 $
2. $\tilde{B}_t$ is a Martingale under $Q$ with continuous sample paths
3. $\tilde{B}_t^2 -t$ is a Martingale

The first requirement is obviously satisfied (by definition).
To show 2 we use Bayes' Theorem for stochastic processes (**TODO**)

$$
	E^Q \left[ \tilde{B}_t | \mathscr{F}_s \right] = \frac{E^P \left[ Z_t \tilde{B}_t | \mathscr{F}_s \right]}{E^P \left[ Z_t | \mathscr{F}_s \right]}
$$

we know that the denominator is a Martingale so we need to show that the numerator is as well, and then 

$$
	\frac{E^P \left[ Z_t \tilde{B}_t | \mathscr{F}_s \right]}{E^P \left[ Z_t | \mathscr{F}_s \right]} = \frac{Z_s \tilde{B}_s}{Z_s} = \tilde{B}_s
$$

Using Ito's lemma again 

$$
\begin{align}
	Z_t = e^{ \mu B_t - \frac{1}{2} \mu^2 t } &\qquad \tilde{B}_t = B_t \mu t \\
	dZ_t = \mu Z_t dB &\qquad d\tilde{B} - \mu dt
\end{align}
$$

and Ito's product rule

$$
\begin{align}
	d(Z_t \tilde{B}_t) &= Z_t d\tilde{B} + \tilde{B}dZ_t + dZ_t d\tilde{B} \\
	&= Z_t (dB - \mu dt) + (B_t -\mu t) \mu Z_t dB + \mu Z_t dB (dB - \mu dt) \\
	&= Z_t dB -\mu Z_t dt + (B_t-\mu t) \mu Z_t dB + \mu Z_t dt \\
	&= \left( Z_t + (B - \mu t) \mu \right)dB
\end{align}
$$

and so we have a driftless Ito diffusion.
Hence $E^P \left[ Z_t \tilde{B}_t | \mathscr{F}_s \right]$ is a Martingale and so $E^Q \left[ \tilde{B}_t | \mathscr{F}_s \right]$ is a Martingale.

Finally using Bayes' theorem again for the third condition

$$
	E^Q \left[ \tilde{B}_t^2 - t | \mathscr{F}_s\right] = \frac{E^P \left[ Z_t \left(\tilde{B}_t^2 -t \right) | \mathscr{F}_s \right]}{E^P \left[ Z_t | \mathscr{F}_s \right]}
$$

and so again we only need to show that $Z_t \left(\tilde{B}_t^2 -t \right)$ is a Martingale.
It goes just the same as for the second requirement so skipping all of the algebra we get

$$
	d\left(Z_t \left(\tilde{B}_t^2 -t \right) \right) = \left( 2Z_t (B- \mu t) + \mu \left(\tilde{B}_t^2 -t \right)Z\right)dB
$$

a driftless Ito diffusion.

