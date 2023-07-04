import pandas as pd
import numpy as np

data = np.random.randn(5, 3)
columns = ["A", "B", "C"]
index = pd.date_range("2023-07-04", periods=5)

df = pd.DataFrame(data, index=index, columns=columns)
print(df)