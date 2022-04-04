#!/bin/bash

DST=../thunderbird-website/media/caldata

if [ ! -e $DST ]; then
    echo Missing fork $DST
    exit 1
fi
cp -a NederlandseFeestdagen.ics $DST/DutchHolidays.ics
cp -a DutchHolidays.ics $DST/DutchHolidaysEnglish.ics
cp -a NiederlaendischeFeiertage.ics $DST/DutchHolidaysGerman.ics
cp -a VacacionesHolandesas.ics $DST/DutchHolidaysFrench.ics
