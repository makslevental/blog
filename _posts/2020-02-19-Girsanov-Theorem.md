---
layout: post
title: Girsanov Theorem
published: true
---

Consider a collection random variables 

$$
	X_0, X_1, X_2, \dots, X_n
$$

where the indices can be taken to correspond with discrete times

$$
	t_0 < t_1 < t_2 < \cdots < t_n
$$

Assume that $P(X_0 = 0) = 1$ and that increments $\Delta X_i := X_{i+1} - X_i$ are distributed Normal

$$
	\Delta X_i \sim N(0, \Delta t_i)
$$

where $\Delta t_i := t_{i+1} - t_i$.

A mechanical procedure for generating $X_i$ is to start at zero, draw an increment some time $\Delta t$ later, add it to the previous total sum, and repeat.
Here's what several such trajectories (*sample paths*) look like

![]({{ "/images/brownian.png" | absolute_url }})

The conditional distribution of $X_i$ given $X_{i-1}$, i.e. given its previous value, is

$$
\begin{align}
	X_i | (X_{i-1} = x_{i-1}) &\sim N(x_{i-1}, \Delta t) \\
	& \iff \\
	p(x_i - x_{i-1} | x_{i-1}) &= \frac{1}{\sqrt{2\pi \Delta t}} \exp \left( -\frac{1}{2\Delta t} \left( x_i - x_{i-1} \right)^2 \right)
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
	&= \frac{1}{(2\pi \Delta t)^{n/2}}\int\limits_{\alpha_1}^{\beta_1}\int\limits_{\alpha_2}^{\beta_2}\cdots\int\limits_{\alpha_n}^{\beta_n} \exp \left( -\frac{1}{2\Delta t} \sum_{i=1}^{n} (x_i - x_{i-1})^2\right) dx_1 dx_2 \cdots dx_n
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
& \int\limits_{ \alpha_1 -\mu_1 \Delta t}^{\beta_1 -\mu_1 \Delta t}\int\limits_{ \alpha_2 - (\mu_1 + \mu_2)\Delta t}^{ \beta_2 - (\mu_1 + \mu_2)\Delta t} \exp \left( -\frac{1}{2\Delta t} (x_1-x_0)^2\right) \exp \left( -\frac{1}{2\Delta t}(x_2-x_1)^2 \right) dx_1 dx_2 
\end{align}
$$

Then $y_1 = x_1 + \mu_1 \Delta $ implies

$$
\begin{align}
& \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 - (\mu_1 + \mu_2)\Delta t}^{ \beta_2 - (\mu_1 + \mu_2)\Delta t} \exp \left( -\frac{1}{2\Delta t} (y_1-x_0-\mu_1 \Delta t)^2\right) \exp \left( -\frac{1}{2\Delta t}(x_2-y_1+\mu_1\Delta t)^2 \right) dy_1 dx_2 
\end{align}
$$

and $y_2 = x_2 + (\mu_1 + \mu_2) \Delta t$ implies

$$
\begin{align}
& \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta } \exp \left( -\frac{1}{2\Delta t} (y_1-x_0-\mu_1 \Delta t)^2\right) \exp \left( -\frac{1}{2\Delta t}(y_2-(\mu_1+\mu_2)\Delta t-y_1+\mu_1\Delta t)^2 \right) dy_1 dy_2 \\
& \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta } \exp \left( -\frac{1}{2\Delta t} (y_1-x_0-\mu_1 \Delta t)^2\right) \exp \left( -\frac{1}{2\Delta t}(y_2-y_1-\mu_2 \Delta t)^2 \right) dy_1 dy_2 
\end{align}
$$

Then changing the dummy variable $y_i \rightarrow x_i$

$$
\begin{align}
& \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta } \exp \left( -\frac{1}{2\Delta t} (x_1-x_0-\mu_1 \Delta t)^2\right) \exp \left( -\frac{1}{2\Delta t}(x_2-x_1-\mu_2 \Delta t)^2 \right) dx_1 dx_2  \\
& \int\limits_{ \alpha_1 }^{\beta_1 }\int\limits_{ \alpha_2 }^{ \beta } \exp \left( -\frac{1}{2\Delta t} \left(\sum_{i=1}^2 x_i - x_{i-1} -\mu_i \Delta t\right)^2\right) dx_1 dx_2

\end{align}
$$
