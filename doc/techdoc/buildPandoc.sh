#!/bin/bash

# ctw 2024.10.22
# produces a .PDF, a .DOCX, and a .HTML from a .MD using pandoc

[ "${#@}" = 0 ]         && echo 'ERROR: no target file given' && exit 1
[ ! -f "$1" ]           && echo "ERROR: could not find $1"    && exit 2
[[ ! "$1" =~ .+'.md' ]] && echo "ERROR: $1 not markdown file" && exit 3

XMARGIN='1.5in'
YMARGIN='1.25in'

METADATA=(
    # article, scrartcl
    'documentclass:scrartcl'
    "margin-left:$XMARGIN"
    "margin-right:$XMARGIN"
    "margin-top:$YMARGIN"
    "margin-bottom:$YMARGIN"
    'colorlinks:true'
    'linestretch:1'
    'fontsize:10pt'
    # empty, headings, plain
    'pagestyle:plain'
    # bookman is very old; palatino, tgschola and utopia are very new; tgtermes
    # and mathptmx are in the middle; lmodern is the default
    # lmodern, tgtermes, bookman, charter, palatino, utopia, mathptmx, tgschola
    'fontfamily:palatino'
)

# maps each attribute to a flag (i.e. `--metadata=<attribute>`)
for ((i=0; i<"${#METADATA[@]}"; i++))
do METADATA["$i"]="--metadata=${METADATA[$i]}"
done

# produce the PDF
pandoc -so "$1.pdf" "$1" "${METADATA[@]}"
pandoc -so "$1.html" "$1" "${METADATA[@]}"
pandoc -so "$1.docx" "$1" "${METADATA[@]}"

exit 0
