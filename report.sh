echo -e 'Dutch holidays:'
grep SUMMARY NederlandseFeestdagen.ics|sed -e 's/SUMMARY://'|sort|uniq 
echo -e '\nEnglish translations of Dutch holidays:'
grep SUMMARY DutchHolidays.ics|sed -e 's/SUMMARY://'|sort|uniq 
echo -e '\nGerman translation of Dutch holidays:'
grep SUMMARY NiederlaendischeFeiertage.ics|sed -e 's/SUMMARY://'|sort|uniq 

echo -e '\n\nDutch categories:'
grep CATEGORIES NederlandseFeestdagen.ics|sed -e 's/CATEGORIES://'|sort|uniq 
echo -e '\nEnglish translations of Dutch categories:'
grep CATEGORIES DutchHolidays.ics|sed -e 's/CATEGORIES://'|sort|uniq 
echo -e '\nGerman translations of Dutch categories:'
grep CATEGORIES NiederlaendischeFeiertage.ics|sed -e 's/CATEGORIES://'|sort|uniq 

wc -l *ics
