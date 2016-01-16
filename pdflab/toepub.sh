python latexExpand.py $1 | pandoc --from=latex -o "${1%%.*}".epub
