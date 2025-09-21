import math as m
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

N = 60
p = 2/3
q = 1/3

x = []
yp = []
yg = []
Nmax = N*(2/3)
var = N*(2/3)*(1/3)
Po = m.sqrt(1/(2*m.pi*var))

for i in range(N):
    n1 = i + 1
    n2 = N - n1
    n3 = n1 - Nmax
    x.append(n1/N)
    PN = (m.factorial(N)/(m.factorial(n1)*m.factorial(n2)))*(p**n1)*(q**n2)
    yp.append(PN)
    PG = Po*m.exp(-(n3**2)/(2*var))
    yg.append(PG)

fig, ax = plt.subplots()
ax.plot(x,yp, color='red', label='Distribuição Binomial')
ax.plot(x,yg, color='blue', label='Distribuição Gaussiana')

ax.set(xlabel='N1/N', ylabel='P(N1)', title='P(N1) x N1/N para N = 60')
ax.grid()

plt.legend(loc='upper left')

fig.savefig("N60PGxN1.jpg")
plt.show()
