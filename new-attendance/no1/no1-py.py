import pandas as pd

longley = pd.read_csv('./longley.csv')
print(longley)

import seaborn as sns

sns.pairplot(longley.iloc[:, 1:])
