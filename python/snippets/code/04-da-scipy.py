import numpy as np
from scipy.integrate import quad


def mfunc(data):
    return np.exp(-(data ** 2))


res, err = quad(mfunc, -np.inf, np.inf)
print(f"Result: {res}")
print(f"Error: {err}")

