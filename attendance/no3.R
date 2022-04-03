# 2번 문제

data <- read.csv('./mvadata/favoritesujects.csv')

library(psych)
library(GPArotation)

data_factor <- principal(data, rotate='none')

factor_varimax <- principal(data, nfactors=3, rotate='varimax', scores=T, method='regression')
