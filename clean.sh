s="            "
echo "Pressure, $s temp, $s Humidity, $s time" > cleanoutput.txt
column -t -s',' output.txt >> cleanoutput.txt
