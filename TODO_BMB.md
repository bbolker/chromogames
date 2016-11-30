
# 30 November 2016

- snowdrift/hawk-dove:
   - several payoff matrices *
   - several starting values *
   - several neighbourhood sizes

no recombination, no colour discrim (b fixed to 0)

expectations: for large nbrhd, regardless of starting value,
  equilibrium is equal to computed eq based on the payoff matrix
for smaller nbrhds, equilibrium is 'nicer' than baseline value

construct a table:

3 payoffs x 3 starting values x 3 nbrhds
run for 5,000 steps, take the average and std err over the last 1000 steps
 (or something else similarly sensible)

e.g. payoff 1 = {3,2,1,7}

payoff "start_value" "nbrhd_size"  "mean"  "lwr" "upr"
1      0.1           5           (mean value, +/- 2 std err OR quantiles)
1      0.5           5
1      0.9           5 
1      0.1           20
1      0.5           20
1      0.9           20
2  ...
2
2



