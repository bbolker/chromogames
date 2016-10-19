
.PHONY : dats
dats : *check.txt

## general rule??
%check.txt: %test.py ../models/EvoAlt.py
	python $*test.py > $*check.txt

## Arangecheck.txt : Arangetest.py
## 	python Arangetest.py > Arangecheck.txt

.PHONY : clean
clean :
	rm *.txt
        
