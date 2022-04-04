# 2번 문제

data <- read.csv('./mvadata/favoritesujects.csv')[-1]

library(psych)
library(GPArotation)

data_factor <- principal(data, rotate='none')
data_factor$values


data_factor$values / sum(data_factor$values)

data_factor$Structure

factor_varimax <- principal(data, nfactors=3, rotate='varimax', scores=T, method='regression')
factor_varimax$Structure

#기존 인자 부하행렬확인
data_factor <- principal(data, nfactors = 3, rotate='none')
data_factor$Structure

factor_promax <- principal(data, nfactors=3, rotate='promax', scores=T, method='regression')
factor_promax$Structure