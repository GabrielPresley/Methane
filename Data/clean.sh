: '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
#!/bin/bash
#
output="output.txt"
echo "" > $output                #clear the output file
#
perl -p -i -e 's/^\$[A-Z][A-Z][A-Z][^G][A-Z].*//g;' $1 #remove extra gps data types
sed -i 's/\$[^G]//' $1         #remove lone "$"
sed -i 's/^G.*//' $1
perl -p -i -e 's/^\s*$//g;' $1 #remove empty lines
# (?<=\*..\n).*(\n?=\+) this works but i cant run it with anysthing
# i=0
# last_loop=$
# while read p; do
# 	if [ $last_loop == ${p:0:1} ]; then
# 		sed -i "/$i/d" $1
# 		echo $i
# 	fi
# 	last_loop=${p:0:1}
# 	i=$((i+1))
# done <$1

for i in "+" "@" "#" "%" ":" "&"
do
	regex='(?<=^\'$i').*\b'       #
	grep -oP $regex $1 >> $output #clear the output file and add Methane data
	echo "NEWLINE" >> $output     #place holder for newlines
done

#GPS DATA DECODED BELLOW
grep -oP '\$GPGGA,[0-9.]+' $1 >> $output   #get time data from GPGGA
sed -i 's/\$GPGGA,//g' $output             #Remove extra text
echo "NEWLINE" >> $output                  #place holder for newlines

grep -oP '(?<=,N,).*(?=,W,)' $1 >> $output #get lon data from gpgga
echo "NEWLINE" >> $output                  #place holder for newlines

grep -oP "[0-9]+.[0-9]+,N," $1 >> $output  #get lat data from gpgga
sed -i 's/,N,//g' $output                  #remove ",N," left over from regex
echo "NEWLINE" >> $output                  #place holder for newlines

grep -oP '[0-9]+.[0-9](?=,M,).*(?=,M,)' $1 >> $output #get alt data from gpgga
sed -i 's/,M,.*//g' $output                #remove ",M,.*" left over from regex


sed -i 's/$/,/' $output           #add comma to end of each data point
perl -p -i -e 's/\R//g;' $output  #remove all newlines
sed -i 's/NEWLINE/\n/g' $output   #put newlines back for placeholders
sed -i 's/^,//g' $output          #Remove leading commas
sed -i 's/,$//g' $output          #Remove trailing commas







#IF THESE NUMBERS ARENT ALL THE SAME MEANS SOME DATA POINTS ARE MISSING
cat $output | xargs -I % sh -c 'echo % | tr -cd , | wc -c'
