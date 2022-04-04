import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X1 = [5.935, 1.523, 2.599, 4.009, 4.687, 8.044, 2.766, 6.538, 6.451, 3.314, 3.777, 1.530, 2.768, 6.585]
X2 = [14.2, 13.1, 12.7, 15.2, 14.7, 15.6, 13.3, 17.0, 12.9, 12.2, 13.0, 13.8, 13.6, 14.9]
X3 = [2.265, 0.597, 1.237, 1.649, 2.312, 3.641, 1.244, 2.618, 3.147, 1.606, 2.119, 0.798, 1.336, 2.763]
X4 = [2.27, 0.75, 1.11, 0.81, 2.50, 4.51, 1.03, 2.39, 5.52, 2.18, 2.83, 0.84, 1.75, 1.91]
X5 = [2.91, 2.62, 1.72, 3.02, 2.22, 2.36, 1.97, 1.85, 2.01, 1.82, 1.80, 4.25, 2.64, 3.17]
data = {'X1': X1, 'X2': X2, 'X3': X3, 'X4': X4, 'X5': X5}

pd_data = pd.DataFrame(data)
pd_data.corr()

x = StandardScaler().fit_transform(pd_data)
x = pd.DataFrame(x, columns=['X1', 'X2', 'X3', 'X4', 'X5'])
pca_init = PCA(n_components=len(pd_data.columns))
pca_init.fit(x)

