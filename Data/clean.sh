: '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
# example ./clean.sh input.txt output.txt
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
#^\\r*\nM.*\n.*\n.*\n.*\n.*\n.*\n.*\n*\n%.*

touch /tmp/step0
touch /tmp/step1
touch /tmp/step2
#awk '{n=$2}l1!=n{if(p)print l0; print; p=0}l1==n{p=1}{l0=$0; l1=n}END{print}' $1 > /tmp/step1
#
cat $1 > /tmp/step1
echo "! -CH ! " > /tmp/step2
grep -oP '(?<=\+).*\b' /tmp/step1 >> /tmp/step2
#
echo "! -HMD ! " >> /tmp/step2
grep -oP '(?<=^&).*\b' /tmp/step1 >> /tmp/step2
#
echo "! -°C ! " >> /tmp/step2
grep -oP '(?<=^@).*\b' /tmp/step1 >> /tmp/step2
#
echo "! -hPA ! " >> /tmp/step2
grep -oP '(?<=^#).*\b' /tmp/step1 >> /tmp/step2
#
echo "! -M-UP ! " >> /tmp/step2
grep -oP '(?<=^%).*\b' /tmp/step1 >> /tmp/step2
#
echo "! -LAT ! " >> /tmp/step2
grep -oP '(?<=,A,).*(?=,N,)' /tmp/step1 >> /tmp/step2
#
echo "! -LON ! " >> /tmp/step2
grep -oP '(?<=,N,).*(?=,W,)' /tmp/step1 >> /tmp/step2
#
echo "! -SEC ! " >> /tmp/step2
grep -oP '(?<=^\:).*\b' /tmp/step1 >> /tmp/step2
#
sed -i 's/\(^.\{1,10\}\).*/\1/' /tmp/step2 #Trim lines to x length
#
cat /tmp/step2 | datamash transpose --field-separator=, > $2
#
sed -i 's/^.,//g' $2 #Remove leading commas
sed -i 's/! /\n/g' $2 # replacing "! " "\n" for titles
sed -i 's/^. ,//g' $2 #Remove leading "x ,"
sed -i 's/\\r//g' $2 # reomve /r from end of lines
#

sed -i 's/.$//; s/^.//' $2 #Remove first/last charecters
#
rm /tmp/step1
rm /tmp/step2

sed -i '2~2d' $2 #Remove Lables
sed -i '1d' $2 # Remove Empty First Line
#
length=$(($(head -n 7 $2 | tail -n 1 | sed 's/[^,]//g' | wc -c)-$3 )) # Counts data point in line 7
echo $length
for i in 1 2 3 4 5 6 7 8; do
head -n $i $2 | tail -n 1 | cut -d, -f1-$length >> /tmp/step0
done
#
cat /tmp/step0 > $2
rm /tmp/step0
echo "DONE"
