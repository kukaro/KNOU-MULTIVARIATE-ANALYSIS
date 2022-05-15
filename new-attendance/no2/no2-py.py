import pandas as pd

deug = pd.read_csv('./deug.csv')
deug = deug.iloc[:, 1:]
print(deug.columns)

print(deug.describe())
print(deug.corr())

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(deug)
X = pd.DataFrame(X, columns=deug.columns)
pca_init = PCA(n_components=len(deug.columns))
pca_init.fit(X)

cumsum = [pca_init.explained_variance_ratio_[0]]
for i in range(1, len(pca_init.explained_variance_ratio_)):
    cumsum.append(cumsum[i - 1] + pca_init.explained_variance_ratio_[i])

print(pca_init.explained_variance_)
print(pca_init.explained_variance_ratio_)
print(cumsum)
