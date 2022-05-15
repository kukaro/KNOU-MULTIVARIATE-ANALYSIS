# install.packages('ade4')
library(ade4)
data(deug)
deug.tab <- deug$tab
t(deug.tab)

summary(deug.tab)

cor(deug.tab)

deug.tab.pca <- princomp(deug.tab, cor = T, scores = T)
deug.tab.pca
deug.tab.pca.summary <- summary(deug.tab.pca)
deug.tab.pca.summary

eig.val <- deug.tab.pca$sdev^2
eig.val

prop <- eig.val[eig.val > 1] / sum(eig.val)
cum.prop <- prop
for (i in 2:length(prop)) {
  cum.prop[i] <- cum.prop[i - 1] + cum.prop[i]
}

prop
cum.prop

screeplot(deug.tab.pca, type = 'lines', pch = 19)

biplot(deug.tab.pca, cex=0.7)

write.csv(deug.tab, 'deug.csv')