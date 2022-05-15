import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer

data = pd.read_csv('../../mvadata/favoritesujects.csv').iloc[:, 1:]
data.transpose()

fa = FactorAnalyzer(rotation=None)
fa.fit(data)

ev, v = fa.get_eigenvalues()

print(ev)
print(ev / sum(ev))

FactorAnalyzer(n_factors=2, rotation=None, method='principal').fit(data).loadings_

fa_varimax = FactorAnalyzer(n_factors=2, rotation='varimax', method='principal')
fa_varimax.fit(data)
print(fa_varimax.loadings_)

fa_promax = FactorAnalyzer(n_factors=2, rotation='promax', method='principal')
fa_promax.fit(data)

fa_promax = FactorAnalyzer(n_factors=2, rotation='promax', method='ml')
fa_promax.fit(data)

fa_promax.loadings_