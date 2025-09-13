doc:
	corre -i doc/source.md -o README.md
	pandoc README.md -so doc/www/index.html -d doc/pandoc.yml
