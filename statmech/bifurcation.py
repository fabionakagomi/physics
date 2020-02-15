import matplotlib.pyplot as plt
import numpy as np

"""
Bifurcations are transitions between dynamical states used in nonlinear dynamics.
This is a saddle-node bifurcation defined by
dx/dt = r-x^2 
It has equilibrium points at x_eq = +/- sqrt(r)
and critical condition found by taking the derivative of dx/dt = F(x)
so we get
dF/dx = -2x
so the bifurcation occurs at x=x_eq, which is
dF/dx = 0
"""

def xeq1(r):
    """
    Stable equilibrium
    """
    return np.sqrt(r)

def xeq2(r):
    """
    Unstable equilibrium
    """
    return np.sqrt(r)

# Plot.
fig = plt.figure(figsize=(9,6))
ax1 = fig.add_subplot(1, 1, 1)
domain = linspace(0, 10)
ax1.plot(domain, xeq1(domain), "b-", label = "stable equilibrium", linewidth = 3)
ax1.plot(domain, xeq2(domain), "r--", label = "unstable equilibrium", linewidth = 3)
ax1.legend(loc="upper left")
# Neutral equilibrium point
ax1.plot([0], [0], "go")
ax1.axis([-10, 10, -5, 5])
ax1.set_xlabel("r")
ax1.set_ylabel("x_eq")
ax1.set_title("Saddle-node bifurcation")

# Add black arrows indicating the attracting dynamics of the stable and the 
# repelling dynamics of the unstable equilibrium point. 
ax1.annotate("", xy=(-7, -4), xytext=(-7, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(-5, -4), xytext=(-5, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(-3, -4), xytext=(-3, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(-1, -4), xytext=(-1, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(1, -4), xytext=(1, -1.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(1, 0.7), xytext=(1, -0.7), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(1, 1.5), xytext=(1, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(3, -4), xytext=(3, -2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(3, 1.5), xytext=(3, -1.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(3, 2), xytext=(3, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(5, -4), xytext=(5, -2.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(5, 2), xytext=(5, -2), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(5, 2.5), xytext=(5, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(7, -4), xytext=(7, -3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(7, 2.3), xytext=(7, -2.3), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
ax1.annotate("", xy=(7, 3), xytext=(7, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)

"""
A transcritical bifurcation happens when the equilibrium point "passes through" another one that exchanges their
stabilities. A supercritical pitchfork bifurcation can make a stable equilibrium point split into two stable
and one stable equilibriums.
"""

def xeq1(r):
    """
    First equilibrium point
    """
    return 0

def xeq2(r):
    """
    Second
    """
    return np.sqrt(r)

def xeq3(r):
    """
    Third
    """
    return -np.sqrt(r)

# Plot.
domain1 = linspace(-10, 0)
domain2 = linspace(0, 10)
plt.plot(domain1, xeq1(domain1), "b-", linewidth = 3)
plt.plot(domain2, xeq1(domain2), "r--", linewidth = 3)
plt.plot(domain2, xeq2(domain2), "b-", linewidth = 3)
plt.plot(domain2, xeq3(domain2), "b-", linewidth = 3)
# Neutral equilibrium point
plt.plot([0], [0], "go")
plt.axis([-10, 10, -5, 5])
plt.xlabel("r")
plt.ylabel("x_eq")
plt.title("Supercritical pitchfork bifurcation")

# Add arrows.
plt.annotate("", xy=(0, -1), xytext=(0, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(0, 1), xytext=(0, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(-5, -0.5), xytext=(-5, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(-5, 0.5), xytext=(-5, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(3, 1.5), xytext=(3, 0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(3, -1.5), xytext=(3, -0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(3, 2.2), xytext=(3, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(3, -2.2), xytext=(3, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(7, 2), xytext=(7, 0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(7, -2), xytext=(7, -0.5), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(7, 3), xytext=(7, 4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)
plt.annotate("", xy=(7, -3), xytext=(7, -4), arrowprops=dict(arrowstyle="->",connectionstyle="arc3",lw=1),)

"""
A subcritical pitchfork bifurcation causes the unstable equilibrium point to split into two unstable
and one stable equilibriums. 
"""
