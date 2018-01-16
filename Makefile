all:
	# Tidy
	rm -f book.html
	rm -f book.pdf
	rm -f merged.pdf
	rm -f output.pdf
	rm -rf text2pdf.*

	# Generate Book
	python3 generate.py > book.html

	# Convert to PDF
	pandoc --pdf-engine=lualatex --template=template.latex -V documentclass=report -V papersize:a5 -V geometry:margin=2cm -f html -t latex book.html -o book.tex
	sed -r -i 's/\\begin\{verbatim\}/\\begin\{lstlisting\}/g' book.tex
	sed -r -i 's/\\end\{verbatim\}/\\end\{lstlisting\}/g' book.tex
	sed -r -i 's/\\includegraphics\{/\\includegraphics[width=\\maxwidth\{\\textwidth\}]\{/g' book.tex
	# sed -r -i 's/KwoC9R4okhg5qP1VqFU2spoileropenC7zVHSK1ZM3Jvkg9atqK/\\begin{rotate}{180}/g' book.tex
	# sed -r -i 's/KwoC9R4okhg5qP1VqFU2spoilercloseC7zVHSK1ZM3Jvkg9atqK/\\end{rotate}/g' book.tex
	pandoc --pdf-engine=lualatex --template=template.latex -V documentclass=report -V papersize:a5 -V geometry:margin=2cm -f latex book.tex -o book.pdf

	# Merge with cover
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=merged.pdf cover.pdf book.pdf

cover:
	convert cover.png cover.pdf

clean:
	# Tidy
	rm -f book.html
	rm -f book.pdf
	rm -f merged.pdf
	rm -f output.pdf
	rm -rf text2pdf.*
