: '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
# example ./clean.sh datatata cartestdata transposedcardata
# middle file is just a step between
#grep
    #   grep  searches  for  PATTERNS  in  each  FILE.
#echo
    #   Echo the STRING(s) to standard output.
#cat
    #   Concatenate FILE(s) to standard output. (like echo for text files)
# $1-3
    #   Arguments used when running script
# -o, --only-matching
    #    Print  only  the  matched (non-empty) parts of a matching line,
    #    with each such part on a separate output line.
# -P, --perl-regexp
    #    Interpret  PATTERNS  as Perl-compatible regular expressions (PCREs).
# ?<=
    #   tells the regex engine to temporarily step backwards in the string,
    #   to check if the text inside the lookbehind can be matched there.
#.*
    #   Select from here to end of line
# > or >>
    # Replace all text in file, and concatenate respectively
grep -oP '(?<=^!).*' $1 >> $2
#
grep -oP '(?<=^&).*' $1 >> $2
#
grep -oP '(?<=^@).*' $1 >> $2
#
grep -oP '(?<=^#).*' $1 >> $2
#
grep -oP '(?<=^%).*' $1 >> $2
#
grep -oP '(?<=,A,).*(?=,N,)' $1 >> $2
#
grep -oP '(?<=,N,).*(?=,W,)' $1 >> $2
#
cat $2 | datamash transpose --field-separator=, > $3
sed -i 's/^.,//g' $3
sed -i 's/^. ,//g' $3
echo "DONE"
