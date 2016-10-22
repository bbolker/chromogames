- `*test.py` files contain python code that run tests on `EvoAlt`. The first comment in the code says what is being tested.  
- the `*check.txt` are the output of the previously mentioned tests. A test fails if the last line of the check.txt file says 'failure'. Else the test was successful. 

===== Tests =====

1) Arangetest : Testing if all elements of parAlst are in [al,au] if mutation for A is turned off.

2) assertest : Verifying that the npy file is the same as running the actual simulation 

3) constantAzeromuttest : Testing if there will be equal reproductive success between competing cells when all cells have the same probability to cooperate and mutation is off. 

4) equalreproductiontest : Testing if reproductive success for all competing cells is equal if A constant, B=0 and mutation for A turned off. 

5) RSTPtest : Testing if the expected value of the payoff is reasonable (ie less than or equal to the sum of the 4 possible payoffs) 

6) storagetest : Testing if the number of cells remains constant. 

7) zeroGametest : Testing if reproductive success for all competing cells is equal if R=P=S=T=0. 
