PATH=/usr/local/texlive/2013/bin/i386-linux:$PATH
python regenerateIndex.py
python xolopes.py
python xolopes.py draft
pdflatex xolopes.tex
pdflatex xolopes.tex
pdflatex draft.tex
pdflatex draft.tex
