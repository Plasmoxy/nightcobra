import pylab
import numpy as np

xspace = np.linspace(-10, 10, 100)

sigmoid = lambda x: 1/(1 + np.e**-x)
f = lambda x: x**2

pylab.plot(xspace, sigmoid(xspace), )
pylab.plot(xspace, f(xspace))
pylab.plot(xspace, pylab.sin(xspace))
pylab.plot(3, sigmoid(3), 'ro')
pylab.plot(3, sigmoid(3), 'ro')

pylab.grid(True)
pylab.ylim(-5, 20)
pylab.show()