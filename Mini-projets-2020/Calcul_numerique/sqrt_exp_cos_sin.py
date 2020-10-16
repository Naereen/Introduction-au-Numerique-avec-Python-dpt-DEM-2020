# coding: utf-8
"""
Implements manually the sqrt(), exp(), cos() and sin() functions.

@author: Lilian Besson
@date: 26-09-2020
@license: MIT
"""

## Square root

def sqrt(x, epsilon=1e-12, maxiter=100, x0=None):
    """ Computes an approximation of sqrt(x) with Héron's method."""
    # initial guess of sqrt_x as floor(sqrt(x)) by a simple loop
    assert x >= 0
    if x == 0: return 0
    if x0 is None:
        sqrt_x = 1.0
        while sqrt_x**2 < x:
            sqrt_x += 1
    else:
        sqrt_x = x0
    # now Héron's method
    nbiter = 0
    while (sqrt_x**2 - x) > epsilon and nbiter < maxiter:
        nbiter += 1
        sqrt_x = (sqrt_x + x / sqrt_x) / 2.0
    return sqrt_x


if __name__ == '__main__':
    for i in range(1, 1000):
        sqrt_i = sqrt(i)
        print(f"sqrt of {i} is computed ~= {sqrt_i}, that's a relative precision of {abs(sqrt_i**2 - i) / i}")


## Now exponential


def factorial(n):
    """ Naive computation of factorial(n) with products. Not recursive."""
    if n <= 0: return 1.0
    else:
        f = 1.0
        for i in range(2, n+1):
            f *= i
        return float(f)

import math

if __name__ == '__main__':
    for i in range(1, 10):
        print(f"{i}! = {factorial(i)}")


def exp(x, epsilon=1e-16, maxiter=100):
    """ Computes an approximation of exp(x) using its series."""
    epsilon = epsilon * x  # relative precision
    nbiter = 1
    exp_x = 1.0
    x_power_n = x
    factorial_n = 1.0
    delta_exp_x = x_power_n / factorial_n
    while delta_exp_x > epsilon and nbiter < maxiter:
        exp_x += delta_exp_x
        nbiter += 1
        x_power_n *= x
        factorial_n *= nbiter
        delta_exp_x = x_power_n / factorial_n
    return exp_x

if __name__ == '__main__':
    for i in range(1, 50):
        exp_i = exp(i)
        true_exp_i = math.exp(i)
        print(f"exp of {i} is computed ~= {exp_i}, that's a relative precision of {abs(exp_i - true_exp_i) / true_exp_i:.2g}")


# Cosine

def cos(x, epsilon=1e-16, maxiter=50):
    """ Computes an approximation of cos(x) using its series."""
    epsilon = epsilon
    x %= 2*math.pi         # put x in [0,2pi] to ensure convergence
    square_x = x*x         # only computer once
    nbiter = 0
    cos_x = 0.0
    x_power_2n = 1.0
    factorial_2n = 1.0
    delta_cos_x = ((-1)**nbiter) * x_power_2n / factorial_2n
    while abs(delta_cos_x-cos_x)/max(abs(cos_x),1.0) > epsilon and nbiter < 2*maxiter:
        cos_x += delta_cos_x
        nbiter += 1
        x_power_2n *= square_x
        factorial_2n *= (2*nbiter - 1) * (2*nbiter)
        delta_cos_x = ((-1)**nbiter) * x_power_2n / factorial_2n
    return cos_x


if __name__ == '__main__':
    for i in range(1, 500):
        cos_i = cos(i)
        true_cos_i = math.cos(i)
        print(f"cos of {i} is computed ~= {cos_i}, that's a relative precision of {abs(cos_i - true_cos_i) / true_cos_i:.2g}")


# Sinus

def sin(x, epsilon=1e-16, maxiter=50):
    """ Computes an approximation of cos(x) using its series."""
    epsilon = epsilon
    x %= 2*math.pi         # put x in [0,2pi] to ensure convergence
    square_x = x*x         # only computer once
    nbiter = 0
    sin_x = 0.0
    x_power_2np1 = float(x)
    factorial_2np1 = 1.0
    delta_sin_x = ((-1)**nbiter) * x_power_2np1 / factorial_2np1
    while abs(delta_sin_x - sin_x)/max(abs(sin_x),1.0) > epsilon and nbiter < 2*maxiter:
        sin_x += delta_sin_x
        nbiter += 1
        x_power_2np1 *= square_x
        factorial_2np1 *= (2*nbiter) * (2*nbiter + 1)
        delta_sin_x = ((-1)**nbiter) * x_power_2np1 / factorial_2np1
    return sin_x


for i in range(1, 500):
    sin_i = sin(i)
    true_sin_i = math.sin(i)
    print(f"sin of {i} is computed ~= {sin_i}, that's a relative precision of {abs(sin_i - true_sin_i) / true_sin_i:.2g}")


if __name__ == '__main__':
    import random
    from IPython import get_ipython
    def timeit(code):
        print(f"\nTiming {code}...")
        return get_ipython().run_line_magic('timeit', code)
    timeit('sqrt(random.random())')
    timeit('math.sqrt(random.random())')

    timeit('exp(random.random())')
    timeit('math.exp(random.random())')

    timeit('cos(random.random())')
    timeit('math.cos(random.random())')

    timeit('sin(random.random())')
    timeit('math.sin(random.random())')


    timeit('sqrt(random.random()) + exp(random.random()) + cos(random.random()) + sin(random.random())')
    timeit('math.sqrt(random.random()) + math.exp(random.random()) + math.cos(random.random()) + math.sin(random.random())')
    timeit('sqrt(1000*random.random()) + exp(10*random.random()) + cos(1000*random.random()) + sin(1000*random.random())')
    timeit('math.sqrt(1000*random.random()) + math.exp(10*random.random()) + math.cos(1000*random.random()) + math.sin(1000*random.random())')

    timeit('sqrt(exp(cos(sin(random.random()))))')
    timeit('math.sqrt(math.exp(math.cos(math.sin(random.random()))))')
    timeit('sqrt(exp(cos(sin(1000*random.random()))))')
    timeit('math.sqrt(math.exp(math.cos(math.sin(1000*random.random()))))')
