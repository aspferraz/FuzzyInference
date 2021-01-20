import numpy as np

_domain = np.linspace(0.5, 10, num=500)
print(_domain)
x_val = 2

ajusted = _domain[np.abs(_domain - x_val).argmin()]
print(ajusted)

