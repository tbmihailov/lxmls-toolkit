import numpy as np

import matplotlib.pyplot as plt
plt.interactive(False)


def get_y(x):
    return (x+2)**2 - 16*np.exp(-((x-2)**2))

x = np.arange(-8, 8, 0.001)
y = map(lambda u: get_y(u), x)
plt.plot(x, y)

def get_grad(x):
    return (2*x+4)-16*(-2*x + 4)*np.exp(-((x-2)**2))

deriv_x = map(lambda u:get_grad(u), x)

def gradient_descent(start_x, func, grad):
    #preceision of the solution
    prec = 0.0001

    step_size = 0.1

    max_iter = 100

    x_new = start_x
    res = []
    for i in xrange(max_iter):
        x_old = x_new

        #use beta equal to -1 for gradient descent
        x_new = x_old - step_size * grad(x_new)

        f_x_new = func(x_new)
        f_x_old = func(x_old)

        res.append([x_new, f_x_new])
        if (abs(f_x_new - f_x_old)< prec):
            print "Change in function values too small..leaving"
            return np.array(res)

    print "Exceeded maximum number of iter"

    return np.array(res)

x_0 = 8
res = gradient_descent(x_0, get_y, get_grad)

#plt.plot(x, deriv_x)

plt.plot(res[:,0], res[:, 1], '+')
plt.show()