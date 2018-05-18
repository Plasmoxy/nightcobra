import pylab
import numpy as np

xspace = np.linspace(-10, 10, 100)

sigmoid = lambda x: 100/(1 + np.e**-x)
f = lambda x: x**2

pylab.plot(xspace, sigmoid(xspace), )
pylab.plot(xspace, f(xspace))
pylab.plot(xspace, 100*pylab.sin(xspace))
pylab.plot(3, sigmoid(3), 'ro')
pylab.plot(3, sigmoid(3), 'ro')

pylab.show()