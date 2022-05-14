data(longley)

t(longley)

# write.csv(longley, file= 'longley.csv')

# 산점도행렬
pairs(longley)
# 별그림
stars(longley)
# 얼굴그림
library(aplpack)
faces(longley)