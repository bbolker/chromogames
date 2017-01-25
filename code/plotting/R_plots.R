npy_dir <- "NPY_files/new"
flist <- list.files(npy_dir,pattern="\\.npy$")
## install.packages("RcppCNPy")
library(RcppCNPy)
x <- npyLoad(file.path(npy_dir,flist[1]))
## assign names
## c("A","colour","fitness","B")  x c("mean","sd")
## saved bogus zero row at beginning?
x <- x[-1,]
library(ggplot2)

matplot(x[,1:4],lty=1,type="l")
