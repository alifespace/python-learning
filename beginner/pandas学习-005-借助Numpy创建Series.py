import numpy as np
import pandas as pd

s = pd.Series(np.arange(10, 100, 10), index=np.arange(101, 110), dtype=float)

print(s)