#!/bin/bash

# builds our techdoc

NAME='techdoc'

# if .TEX file does not exist, throw an error
[ ! -f "$NAME.tex" ] && echo "ERROR: could not locate .TEX" && exit 1

# generate the .PDF
pdflatex "$NAME.tex"
pdflatex "$NAME.tex"

# marked for death
MARKED=(
  'aux'
  'log'
  'out'
  'toc'
  'fdb_latexmk'
  'fls'
)

# if marked file exists, remove it
for EXT in "${MARKED[@]}"
do
  [ -f "$NAME.$EXT" ] && rm "$NAME.$EXT"
done
