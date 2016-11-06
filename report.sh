grep SUMMARY NederlandseFeestdagen.ics|sed -e 's/SUMMARY://'|sort|uniq>names-used-dutch.txt
grep SUMMARY DutchHolidays.ics|sed -e 's/SUMMARY://'|sort|uniq>names-used-english.txt
grep SUMMARY NiederlaendischUrlaub.ics|sed -e 's/SUMMARY://'|sort|uniq>names-used-german.txt
