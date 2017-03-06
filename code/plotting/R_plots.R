library(RcppCNPy)
library(tidyr)
library(dplyr)
library(tibble)
library(ggplot2)

npy_dir <- "NPY_files/new"
flist <- list.files(npy_dir,pattern="\\.npy$")
flist <- flist[1:3]  ## temporarily skip last file - empty?

n0 <- outer(c("A","B","colour","fitness"),c("mean","sd"),paste,sep="_")

get_file <- function(f,path=npy_dir) {
    r <- npyLoad(file.path(path,f))  ## load file
    ## now add column names and a time column
    r <- r %>% as_tibble %>% setNames(n0) %>% mutate(t=1:n())
    return(r)
}
    
alldat <- lapply(flist,get_file) %>%
    setNames(flist) %>%
    bind_rows(.id="file") %>%                  ## combine all files
    mutate(file=gsub("\\.npy$","",file)) %>%   ## drop .npy extension
    separate(file,into=c("gametype","nbrsize","ic"))

alldat2 <- alldat %>% select(gametype,nbrsize,ic,t,A_mean,A_sd)

alldat3 <- alldat2 %>%
    filter(t>50000) %>%
    gather(var,val,c(A_mean,A_sd)) %>%  ## change to long format
    group_by(gametype,nbrsize,ic,var) %>%       ## do some operation for each var
    summarise(mean=mean(val),
              sd=sd(val))

ggplot(alldat3,aes(nbrsize,mean))+
    geom_pointrange(aes(ymin=mean-2*sd,ymax=mean+2*sd))+
    facet_wrap(~var,scale="free")



