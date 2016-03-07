#!/usr/bin/env python3
"""
Name		generate.py
Description	Generate ICS files in Dutch and English for Dutch holidays
Author		Pander <pander@users.sourceforge.net>
License		Public domain

0.1 2013-05-10	Pander <pander@users.sourceforge.net>
Initial release

0.2 2016-03-07	Pander <pander@users.sourceforge.net>
Ported to Python 3
"""

from datetime import datetime, timedelta
from os import listdir

kalender = open('NederlandseFeestdagen.ics', 'w')
calendar = open('DutchHolidays.ics', 'w')

calendar_header = open('templates/calendar-header.txt', 'r')
for line in calendar_header.readlines():
    kalender.write(line)
    calendar.write(line.replace('NederlandseFeestdagen', 'DutchHolidays'))

holiday_header = ''
event_header = open('templates/event-header.txt', 'r')
for line in event_header.readlines():
    holiday_header += line

holiday_footer = ''
event_footer = open('templates/event-footer.txt', 'r')
for line in event_footer.readlines():
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open(directory + '/' + holiday_file, 'r')
        (naam, name) = holiday_file[:-4].split('_')
        kalender.write(holiday_header.strip()+naam+'\n')
        calendar.write(holiday_header.strip()+naam+' ('+name+')\n')
        for line in holiday.readlines():
            kalender.write(line)
            calendar.write(line)
        if 'Nieuwjaarsdag' in naam or 'Goede Vrijdag' in naam or 'Paasdag' in naam or 'Koning' in naam or 'Bevrijdinsdag' in naam or 'Hemelvaartsdag' in naam or 'Pinksterdag' in naam or 'Kerstdag' in naam:
            kalender.write(holiday_footer)
            calendar.write(holiday_footer)
        else:
            kalender.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))
            calendar.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))

directory = 'unscripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open(directory + '/' + holiday_file, 'r')
        (naam, name) = holiday_file[:-4].split('_')
        for line in holiday.readlines():
            kalender.write(holiday_header.strip()+naam+'\n')
            calendar.write(holiday_header.strip()+naam+' ('+name+')\n')
            date = datetime.strptime(line.strip(), '%Y%m%d')
            kalender.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendar.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            if naam == 'Carnaval':
                date += timedelta(days=3)
            else:
                date += timedelta(days=1)
            kalender.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendar.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            if 'Nieuwjaarsdag' in naam or 'Goede Vrijdag' in naam or 'Paasdag' in naam or 'Koning' in naam or 'Bevrijdinsdag' in naam or 'Hemelvaartsdag' in naam or 'Pinksterdag' in naam or 'Kerstdag' in naam:
                kalender.write(holiday_footer)
                calendar.write(holiday_footer)
            else:
                kalender.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))
                calendar.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))

calendar_footer = open('templates/calendar-footer.txt', 'r')
for line in calendar_footer.readlines():
    kalender.write(line)
    calendar.write(line)
