import math as m
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

N = 60
p = 2/3
q = 1/3

x = []
y = []

for i in range(N):
    n1 = i + 1
    n2 = N - n1
    x.append(n1/N)
    P = (m.factorial(N)/(m.factorial(n1)*m.factorial(n2)))*(p**n1)*(q**n2)
    y.append(P)

fig, ax = plt.subplots()
ax.plot(x,y, color='red')

ax.set(xlabel='N1/N', ylabel='PN(N1)', title='PN(N1) x N1/N para N = 60')
ax.grid()

fig.savefig("PxN1.jpg")
plt.show()
