#!/bin/bash

# builds our techdoc

NAME='techdoc'

# if .TEX file does not exist, throw an error
if [ ! -f "$NAME.tex" ]; then
  echo "ERROR: could not locate .TEX"
  exit 1
fi

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
for EXT in "${MARKED[@]}"; do
  if [ -f "$NAME.$EXT" ]; then
    rm "$NAME.$EXT"
  fi
done
