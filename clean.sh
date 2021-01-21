: '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
echo "" > $2
 grep -oP '(?<=Methane\ \(PPM\)).*' $1 >> $2
 grep -oP '(?<=Humidity\ \(%\)).*' $1 >> $2
 grep -oP '(?<=Temperature\ \(\*c\)).*' $1 >> $2
 grep -oP '(?<=Pressure\ \(hPa\)).*' $1 >> $2
 grep -oP '(?<=Altitude\ \(m\)).*' $1 >> $2
 awk '/^49/' $1 >> $2
 sed -i 's/$/, /' $2

cat $2 | datamash transpose --field-separator=, > $3
