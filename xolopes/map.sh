python getDot.py
dot -Tpdf -Gsize=5.8,8.3 chunks.txt -o chunks.pdf
dot -Tsvg -Gsize=5.8,8.3 chunks.txt -o chunks.svg
dot -Tpng -Gsize=5.8,8.3 chunks.txt -o chunks.png
dot -Tps  -Gsize=5.8,8.3 chunks.txt -o chunks.ps
