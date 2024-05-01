import pandas as pd

s = pd.Series(data=['001', '002', '003', '004'], index=list('abcd'))
print(s)

s1 = s.astype(int)
s2 = s.map(int)
print(s1)
print(s2)