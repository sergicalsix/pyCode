from rich.traceback import install 
install()

import numpy as np

a = np.random.randn(100)
b = np.zeros(100)

print(a/b)
