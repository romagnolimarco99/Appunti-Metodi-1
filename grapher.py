# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:31:53 2020

@author: berni
"""
import numpy as np
import cmath as cm
from matplotlib import pyplot as plt

# Costanti dei grafici
a = 1
c = 2.
b = 3
eps = 2e-4

xnum = 10000
xx = np.linspace(start=-1, stop=1, num=xnum)

Niter = 30 
Nstep = 5
# Definizione funzioni e successioni

def f_n(x, n):
    return abs(x)**(1. + 1./n)
    # y_n = []
    # for x in xx:
    #     if a <= x <= c - 1./n:
    #         y_n.append(0)
    #     elif (c - 1./n) <= x <= c:
    #         y_n.append(n * (x - c + 1./n))
    #     elif c <= x <= (c + 1./n):
    #         y_n.append(n * (-x + c + 1./n))
    #     elif c + 1./n <= x <= b:
    #         y_n.append(0)
    # return y_n

def f(x):
    return abs(x)
    # y = []
    # for x in xx:
    #     if a <= x < c:
    #         y.append(0)
    #     elif abs(x) <= c + eps:
    #         y.append(1)
    #     elif c < x <= b:
    #         y.append(0)
    # return y

def pi_fmt(value, tick_number):
    # returns number of multiples of pi/2 (argument of FuncFormatter)
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)

    
# Variabili di controllo dei grafici in ordine decrescente di pesantezza
tex=True
tick=True
axes=True
# Impostazioni opzionali per tipografia in LaTeX
if tex:
   plt.rc('text', usetex=True)
   plt.rc('font', family='serif')

# Grafico
fig, ax = plt.subplots()
plt.plot(xx, f(xx), label=r'$ \left| x \right| $', zorder = 10)
plt.plot(xx, f_n(xx, 1), ls='--', alpha=0.8, label=r'$ \left| x \right|^2 $')
# for n in range(5, Niter, Nstep):
for n in [2, 4, 10, 20]:
    plt.plot(xx, f_n(xx, n), ls='--', alpha=0.8,
             label=r'$\left| x \right|^{1 + 1/%d} $' %n)

ax.minorticks_on()
# ax.grid(c = 'gray', ls = '--', alpha=0.7)
# ax.grid(which = 'minor', c = 'gray', ls = '--', alpha=0.4)
ax.set_xlabel('$x$', x=0.9, fontsize=14)
ax.set_ylabel('$f(x)$', y=0.8, rotation=0, fontsize=14)
if axes:
    ax.axhline(0, c='k', lw=1, xmin=0.05, xmax=0.95)
    ax.axvline(0, c='k', lw=1, ymax=0.95)
    ax.scatter(0,1.1, marker = '^', c='k')
    ax.scatter(1.1,0, marker = '>', c='k')
ax.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax.tick_params(which='minor', direction='in', width=1., top=True, right=True)
if tick:
    # ax.set_xlim(a, b)
    # ax.set_ylim(0, 1)
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
    # plt.xticks([1, 2, 3], ['a', 'c', 'b'])
    # ax.xaxis.set_major_formatter(plt.FuncFormatter(pi_fmt))
    # ax.xaxis.set_minor_locator(plt.MultipleLocator(5e-2))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
    # ax.yaxis.set_minor_locator(plt.MultipleLocator(5e-2))
    plt.tight_layout()

legend = ax.legend(loc ='lower left')
fig.show()