# TODO

- combined plots for tests of theoretically predicted homogeneous polymorphic ESS vs. results for different neighb sizes:

   |
   |    |  |
   |   (1)(2)      |
   |    |  |       *       |           |
   | ------------- |-------*---------- *
   |                       |           |
   |__________________________________

    nbsize=1   nbsize=2  nbsize=3  nbsize=4
    (nbrs=4)   (nbrs=12) (nbrs=24)

Moore nbrhood:  n=1 (8), n=2 (24)

on *one graph*, mean +/- 2 se (over time)
(1) and (2) are runs starting at different initial conditions ...

 * = mean value from time 10,000 to end (i.e. mean of spatial mean)
 | = std error, ditto ...

 (can use numpy functions)

also save the output as a table in the following format:
make a numpy array containing the following information:

  run nbr_type init_a nbr_size tot_nbrs mean  SE
  1   0            1  1        8        ***   ***
  2   0            2  1        8        ***   ***
  ....

Run up to 3 jobs in parallel on collywobbles.
Think about runs with b varying.
If your other runs are done, start them.

Read next chapter in textbook ... (chapter 5)

