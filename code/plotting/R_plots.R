library(RcppCNPy)
library(tidyr)
library(dplyr)
library(tibble)
library(ggplot2); theme_set(theme_classic())

npy_dir <- "NPY_files/new"
flist <- list.files(npy_dir,pattern="\\.npy$")

n0 <- outer(c("A","B","colour","fitness"),c("mean","sd"),paste,sep="_")
get_file <- function(f,path=npy_dir) {
    r <- npyLoad(file.path(path,f))  ## load file
    ## now add column names and a time column
    r <- r %>% as_tibble %>% setNames(n0) %>% mutate(t=1:n())
    return(r)
}
    
alldat <- lapply(flist,get_file) %>%           ## get list of files
    setNames(flist)
## sapply(alldat,nrow)

alldat2 <- alldat %>%                        ## set list names 
    bind_rows(.id="file") %>%                  ## combine all files
    mutate(file=gsub("\\.npy$","",file)) %>%   ## drop .npy extension
    ## split filename (without extension) into three pieces of info
    separate(file,into=c("gametype","nbrsize","ic"))

alldat3 <- alldat2 %>% select(gametype,nbrsize,ic,t,A_mean,A_sd)

alldat4 <- alldat3 %>%
    gather(var,val,c(A_mean,A_sd)) %>%  ## change to long format
    group_by(gametype,nbrsize,ic,var)

## we don't really need to plot every single point; thinning
alldat4_thin <- alldat4 %>%
    filter(t %% 100 == 0)

ggplot(alldat4_thin,aes(t,val,colour=nbrsize))+geom_line()+
    facet_wrap(~var)
ggsave("ns_trajectories.pdf",width=8,height=5)

alldat5 <- alldat4 %>%       ## do some operation for each var
    filter(t>max(t)-25000) %>%
    summarise(mean=mean(val),
              sd=sd(val))

ggplot(alldat5,aes(nbrsize,mean))+
    geom_pointrange(aes(ymin=mean-2*sd,ymax=mean+2*sd))+
    facet_wrap(~var,scale="free")+
    labs(x="neighborhood size",y="")
ggsave("ns_summaries.pdf",width=8,height=5)


