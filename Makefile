all:
	rm -f book.txt
	rm -f book.pdf
	rm -rf text2pdf.*
	python3 generate.py > book.txt
	pandoc book.txt --pdf-engine=xelatex -o book.pdf

clean:
	rm -f book.txt
	rm -f book.pdf
	rm -rf text2pdf.*
