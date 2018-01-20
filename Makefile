all: clean cover generate tex pdf

generate:
	# Generate Book
	python3 generate.py > book.html

tex:
	# Convert to PDF
	# pandoc --pdf-engine=lualatex --number-sections --top-level-division=chapter --template=template.latex -V toc -V toc-depth=3 -V documentclass=extreport -V fontsize=9pt -V papersize:a5 -V geometry:margin=0.5in -f html -t latex book.html -o book.tex
	pandoc --pdf-engine=lualatex --number-sections --top-level-division=chapter --template=template.latex -V toc -V toc-depth=1 -V documentclass=extreport -V fontsize=9pt -V papersize:a5 -V geometry:margin=0.5in -f html -t latex book_edited.html -o book.tex
	# Unfinished work, trying to get maths to work.
	# pandoc --pdf-engine=lualatex --number-sections --top-level-division=chapter --template=template.latex -V toc -V toc-depth=1 -V documentclass=extreport -V fontsize=9pt -V papersize:a5 -V geometry:margin=0.5in -f markdown+raw_tex -t latex book.md -o book.tex
	# perl -plne 's/\\\$/\$/g' book.tex > temp.tex
	# perl -plne 's/\\\\/\\/g' temp.tex > book.tex

	# Tidy
	dos2unix book.tex
	sed -r -i 's/\\begin\{verbatim\}/\\begin\{lstlisting\}/g' book.tex
	sed -r -i 's/\\end\{verbatim\}/\\end\{lstlisting\}/g' book.tex

	# New page
	sed -r -i -z 's/\\begin\{center\}\\rule\{0.5\\linewidth\}\{\\linethickness\}\\end\{center\}\n+\\begin\{center\}\\rule\{0.5\\linewidth\}\{\\linethickness\}\\end\{center\}/\\begin\{center\}\\rule\{1.0\\linewidth\}\{\\linethickness\}\\end\{center\}/g' book.tex

	# Make pagerefs
	sed -r -i 's/\\protect\\hypertarget\{question([0-9]+)\}\{\}\{\}/\\label\{question\1\}/g' book.tex
	sed -r -i 's/\\protect\\hypertarget\{solution([0-9]+)\}\{\}\{\}/\\label\{solution\1\}/g' book.tex
	sed -r -i 's/\\protect\\hyperlink\{solution([0-9]+)\}\{[a-zA-Z0-9\-_ ]+\}/Solution on page \\pageref\{solution\1\}./g' book.tex
	sed -r -i 's/\\protect\\hyperlink\{question([0-9]+)\}\{[a-zA-Z0-9\-_ ]+\}/Question on page \\pageref\{question\1\}./g' book.tex
	sed -r -i 's/\\href\{question([0-9]+)\}\{[a-zA-Z0-9\-_ ]+\}/\\pageref\{question\1\}/g' book.tex

pdf:
	# To pdf
	lualatex book.tex
	lualatex book.tex
	lualatex book.tex

	make merge

merge:
	# Merge with cover
	gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=merged.pdf cover.pdf book.pdf

cover:
	# Cover
	convert -density 300 cover.png cover.pdf

clean:
	# Tidy
	rm -f book.aux book.log book.out book.tex.bak book.toc book.pdf output.pdf
	rm -rf text2pdf.*
