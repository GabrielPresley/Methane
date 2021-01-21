: '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|*    This code was written by     |
|*               MMM               |
|*  MMM Monitors Methane was made  |
|*   for grad 2021 BSS SRM Class   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ '
echo "" > $2
 grep -oP '(?<=Methane\ \(PPM\)).*' $1 >> $2
 grep -oP '(?<=Humidity\ \(%\)).*' $1 >> $2
 grep -oP '(?<=Temperature\ \(\*c\)).*' $1 >> $2
 grep -oP '(?<=Pressure\ \(hPa\)).*' $1 >> $2
 grep -oP '(?<=Altitude\ \(m\)).*' $1 >> $2
 grep ^49 $1 >> $2
