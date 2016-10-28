
all : Arangecheck.txt constantAzeromutcheck.txt equalReproductioncheck.txt RSTPcheck.txt storagecheck.txt zeroGamecheck.txt assertcheck.txt 

%check.txt: %.py ../models/EvoAlt.py
	python $*.py > $*check.txt

.PHONY : gits 
gits : 
	git add *

.PHONY : clean
clean :
	git add *check.txt 
	git rm *check.txt
