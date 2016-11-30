
dd <- read.table(header=TRUE,text="
payoff start_value   nbrhd_size  mean  lwr upr
1      0.1           5           6     3   9
1      0.5           5           7     2   9
1      0.9           5           6.5   2   8
1      0.1           20          10    9   11
1      0.5           20          10.5  9   11
1      0.9           20          12    8   13
2      0.1           5           4     3   5
")

library(ggplot2)
ggplot(dd,aes(nbrhd_size,mean,
              colour=factor(payoff),
              shape=factor(start_value)))+
    geom_pointrange(aes(ymin=lwr,ymax=upr))+
    facet_grid(payoff~start_value,labeller=label_both)
