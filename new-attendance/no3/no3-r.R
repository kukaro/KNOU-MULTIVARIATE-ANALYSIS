data <- read.csv('./mvadata/favoritesujects.csv')[-1]

library(psych)
library(GPArotation)

data.factor <- principal(data, rotate = 'none')
data.factor$values

data.factor$values / sum(data.factor$values)

data.varimax <- principal(data, nfactors = 2, rotate = 'varimax', scores = T, method = 'regression')
data.varimax$Structure

data.promax <- principal(data, nfactors = 2, rotate = 'promax', scores = T, method = 'regression')
data.promax

data.factor <- principal(data, nfactors = 2, rotate = 'none')
data.factor$Structure

biplot(data.factor)