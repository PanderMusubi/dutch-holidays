rm -f report.txt

echo -e 'Dutch holidays:'>>report.txt
grep SUMMARY NederlandseFeestdagen.ics|sed -e 's/SUMMARY://'|sort|uniq >>report.txt
echo -e '\nEnglish translations of Dutch holidays:'>>report.txt
grep SUMMARY DutchHolidays.ics|sed -e 's/SUMMARY://'|sort|uniq >>report.txt
echo -e '\nGerman translation of Dutch holidays:'>>report.txt
grep SUMMARY NiederlaendischeFeiertage.ics|sed -e 's/SUMMARY://'|sort|uniq >>report.txt

echo -e '\n\nDutch categories:'>>report.txt
grep CATEGORIES NederlandseFeestdagen.ics|sed -e 's/CATEGORIES://'|sort|uniq >>report.txt
echo -e '\nEnglish translations of Dutch categories:'>>report.txt
grep CATEGORIES DutchHolidays.ics|sed -e 's/CATEGORIES://'|sort|uniq >>report.txt
echo -e '\nGerman translations of Dutch categories:'>>report.txt
grep CATEGORIES NiederlaendischeFeiertage.ics|sed -e 's/CATEGORIES://'|sort|uniq >>report.txt
