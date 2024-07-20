#!/bin/bash

# builds our techdoc

NAME='techdoc'

# if .TEX file does not exist, throw an error
[ ! -f "$NAME.tex" ] && echo "ERROR: could not locate .TEX" && exit 1

# generate the .PDF & write output to a .TEX.LOG
latex -shell-escape "$NAME.tex"
pdflatex -shell-escape "$NAME.tex"

# `-p` for 'preserve files'
[ "$1" = '-p' ] && exit 0

# marked for death
MARKED=(
  'aux'
  'dvi'
  'log'
  'out'
  'out.ps'
  'toc'
  'fdb_latexmk'
  'fls'
)

# if marked file exists, remove it
for EXT in "${MARKED[@]}"
do
  [ -f "$NAME.$EXT" ] && rm "$NAME.$EXT"
done

# kill this guy too
[ -d "_minted-$NAME" ] && rm -r "_minted-$NAME"

exit 0
