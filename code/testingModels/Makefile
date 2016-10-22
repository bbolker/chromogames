
Arangecheck.txt : Arangetest.py ../models/EvoAlt.py variables.py 
	@echo "Testing if all elements of parAlst are in [al,au] if mutation for A is turned off.";
	python Arangetest.py > Arangecheck.txt; 
	@echo "Done"; 

constantAzeromutcheck.txt : constantAzeromuttest.py ../models/EvoAlt.py  
	@echo "Testing if there will be equal reproductive success between competing cells when all cells have the same probability to cooperate and mutation is off."
	python constantAzeromuttest.py > constantAzeromutcheck.txt; 
	@echo "Done"; 

equalReproductioncheck.txt : equalReproductiontest.py ../models/EvoAlt.py  
	@echo "Testing if reproductive success for all competing cells is equal if A constant, B=0 and mutation for A turned off." 
	python equalReproductiontest.py > equalReproductioncheck.txt; 
	@echo "Done"; 

RSTPcheck.txt : RSTPtest.py ../models/EvoAlt.py 
	@echo "Testing if the expected value of the payoff is reasonable (ie less than or equal to the sum of the 4 possible payoffs)" 
	python RSTPtest.py > RSTPcheck.txt; 
	@echo "Done" 

storagecheck.txt : storagetest.py ../models/EvoAlt.py 
	@echo "Testing if the number of cells remains constant." 
	python storagetest.py > storagecheck.txt; 
	@echo "Done" 

zerocheck.txt : zeroGametest.py ../models/EvoAlt.py 
	@echo "Testing if reproductive success for all competing cells is equal if R=P=S=T=0." 
	python zeroGametest.py > zerocheck.txt;
	@echo "Done"  

assertcheck.txt : asserttest.py ../models/EvoAlt.py  
	@echo "Verifying that the npy file is the same as running the actual simulation" 
	python asserttest.py > assertcheck.txt; 
	@echo "Done"    

.PHONY : dats
dats : Arangecheck.txt constantAzeromutcheck.txt equalReproductioncheck.txt RSTPcheck.txt storagecheck.txt zerocheck.txt assertcheck.txt

all : *check.txt 

# general rule?? 
%check.txt: %test.py ../models/EvoAlt.py
	python $*test.py > $*check.txt


.PHONY : clean
clean :
	rm *check.txt
	rm *.npy  
