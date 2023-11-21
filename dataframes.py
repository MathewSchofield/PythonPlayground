import pandas as pd

df1 = pd.DataFrame([1,2,5,6])
df2 = pd.DataFrame([17,27,57,67])

print(pd.concat([df1, df2]))

