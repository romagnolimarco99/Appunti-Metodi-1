# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:31:53 2020

@author: berni
"""

import numpy as np
import cmath as cm
from matplotlib import pyplot as plt

# Costanti dei grafici
a = 1
c = 2
b = 3

xnum = 1000
xx = np.linspace(start=1, stop=3, num=xnum)

Niter = 30 
Nstep = 5
# Definizione funzioni e successioni

def f_n(x, n):
    y_n = []
    for x in xx:
        if a <= x <= c:
            y_n.append(0)
        elif c -1./n <= x <= c + 1./n:
            y_n.append(n/2. * (x - c + 1./n))
        elif c + 1./n <= x <= b:
            y_n.append(1)
    return y_n

def f(x):
    y = []
    for x in xx:
        if a <= x < c:
            y.append(0)
        elif x == c:
            y.append(1./2)
        elif c < x <= b:
            y.append(1)
    return y
    
# Variabili di controllo dei grafici in ordine decrescente di pesantezza
tex=True
tick=False
# Impostazioni opzionali per tipografia in LaTeX
if tex:
   plt.rc('text', usetex=True)
   plt.rc('font', family='serif')

# Grafico
fig, ax = plt.subplots()
plt.plot(xx, f(xx), label='$f(x)$', zorder = 10)
plt.plot(xx, f_n(xx, 1), label='$f_1 (x)$')
# for n in range(5, Niter, Nstep):
for n in [2, 3, 4, 5, 10, 20, 30]:
    plt.plot(xx, f_n(xx, n), label='$f_{%d}(x)$' %n)
ax.grid(color = 'gray', ls = '--', alpha=0.7)
ax.set_xlabel('x', x=0.9)
ax.set_ylabel('y')
ax.minorticks_on()
ax.tick_params(direction='in', length=5, width=1., top=True, right=True)
ax.tick_params(which='minor', direction='in', width=1., top=True, right=True)
if tick:
    ax.set_xlim(0, c)
    # ax.set_ylim(0, 1)
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.2))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(5e-2))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

legend = ax.legend(loc ='best')
fig.show()