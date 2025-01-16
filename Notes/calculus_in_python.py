#%%
from sympy import symbols, diff
from sympy.abc import lamda
import numpy as np

#EXAMPLE FUNC
def f(x):
    return x ** 2
#%%
#DERIVATIVE (Symbolic)
from sympy import symbols, diff
from sympy.abc import lamda

# Define a variable and a function
x = symbols('x')
f_sym = x ** 2

print(f"The derivative of the function is: {diff(f_sym, x)}")
#%%
#DERIVATIVE of function at x (numerical)
def df(func, x, dx=1e-10):
    return (func(x + dx) - func(x - dx)) / (2 * dx)

print(f"The derivative of the function at x=0 is: {df(f, 0)}")
#%%
#INTEGRATE function over [0, 1]
def I(func, n=100000):
    # Monte Carlo Integration
    return np.mean(func(np.random.uniform(0, 1, n)))

print(f"The integral of the function over [0, 1] is: {I(f)}")
#%%
def get_normalized_function(fun):
    return lambda x: fun(x) / I(fun)

# Test the normalized function with a specific value of x (e.g., x = 0.5)
print(f"The normalized f(x) at x={0.5} is: {get_normalized_function(f)(0.5)}")