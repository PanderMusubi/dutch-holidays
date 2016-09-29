#!/usr/bin/env python3
"""
Name		process-holidays.py
Description	Generate ICS files in Dutch and English for Dutch holidays
Author		Pander <pander@users.sourceforge.net>
License		Public domain

0.1 2013-05-10	Pander <pander@users.sourceforge.net>
Initial release

0.2 2016-03-07	Pander <pander@users.sourceforge.net>
Ported to Python 3

0.3 2016-03-07	Pander <pander@users.sourceforge.net>
Added actual DTSTAMP

0.4 2016-09-29	Wouter Haffmans <wouter@simply-life.net>
Generate valid iCal files (UID field added, newlines written as CRLF)
"""

from datetime import datetime, timedelta
from os import listdir
import os
import socket

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')
calendar = open('DutchHolidays.ics', 'w', newline='\r\n')

calendar_header = open('templates/calendar-header.txt', 'r')
for line in calendar_header:
    kalender.write(line)
    calendar.write(line.replace('NederlandseFeestdagen', 'DutchHolidays'))

uid_format='UID:%(date)s-%(pid)d-%(seq)04d-%(lang)s@%(domain)s\n'
uid_replace_values = {
    'date': format(datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')),
    'pid':  os.getpid(),
    'domain': socket.getfqdn()
}
event_seq = 1

holiday_header = ''
event_header = open('templates/event-header.txt', 'r')
for line in event_header:
    holiday_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')))

holiday_footer = ''
event_footer = open('templates/event-footer.txt', 'r')
for line in event_footer:
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file), 'r')
        (naam, name) = holiday_file[:-4].split('_')
        kalender.write(holiday_header.strip()+naam+'\n')
        calendar.write(holiday_header.strip()+naam+' ('+name+')\n')
        kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'nl', 'seq': event_seq }.items()))))
        calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
        event_seq += 1
        for line in holiday:
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
        holiday = open('{}/{}'.format(directory, holiday_file), 'r')
        (naam, name) = holiday_file[:-4].split('_')
        for line in holiday:
            kalender.write(holiday_header.strip()+naam+'\n')
            calendar.write(holiday_header.strip()+naam+' ('+name+')\n')
            kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'nl', 'seq': event_seq }.items()))))
            calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
            event_seq += 1
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
for line in calendar_footer:
    kalender.write(line)
    calendar.write(line)
