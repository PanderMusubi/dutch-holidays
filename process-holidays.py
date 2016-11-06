#!/usr/bin/env python3
"""
Name		process-holidays.py
Description	Generate ICS files in Dutch and English for Dutch holidays
Author		Pander <pander@users.sourceforge.net>
License		Public domain

0.5 2016-11-06	Pander <pander@users.sourceforge.net>
Optimised code, minor improvements and added German translation

0.4 2016-09-29	Wouter Haffmans <wouter@simply-life.net>
Generate valid iCal files (UID field added, newlines written as CRLF)

0.3 2016-03-07	Pander <pander@users.sourceforge.net>
Added actual DTSTAMP

0.2 2016-03-07	Pander <pander@users.sourceforge.net>
Ported to Python 3

0.1 2013-05-10	Pander <pander@users.sourceforge.net>
Initial release
"""

from datetime import datetime, timedelta
from os import getpid, listdir
from socket import getfqdn

# date and time
utcnow = datetime.utcnow()
dtstamp = utcnow.strftime('%Y%m%dT%H%M%SZ')

# event UID
uid_format='UID:%(date)s-%(pid)d-%(seq)04d-%(lang)s@%(domain)s\n'
uid_replace_values = {
    'date': dtstamp,
    'pid':  getpid(),
    'domain': getfqdn()
}
event_seq = 1

# translations
translations = {
'Nederlandse Feestdagen'     : {'en':'Dutch Holidays',
                                'de':'Niederländisch Urlaub'},

'Bevrijdingsdag'             : {'en':'Liberation Day',
                                'de':'Befreiungstag'},
'Carnaval'                   : {'en':'Carnival',
                                'de':'Karneval'},
'Dag van de Arbeid'          : {'en':'May Day',
                                'de':'Tag der Arbeit'},
'Dierendag'                  : {'en':'Animal Day',
                                'de':'Welttierschutztag'},
'Dodenherdenking'            : {'en':'Remembrance of the Dead',
                                'de':'Volkstrauertag'},
'Driekoningen'               : {'en':'Epiphany',
                                'de':'Dreikönigstag'},
'Eerste Kerstdag'            : {'en':'Christmas Day',
                                'de':'Erster Weihnachtsfeiertag'},
'Eerste Paasdag'             : {'en':'Easter Sunday',
                                'de':'Erster Osterfeiertag'},
'Eerste Pinksterdag'         : {'en':'Pentecost Sunday',
                                'de':'Erster Pfingstfeiertag'},
'Goede Vrijdag'              : {'en':'Good Friday',
                                'de':'Karfreitag'},
'Gronings Ontzet'            : {'en':'Siege of Groningen',
                                'de':'Groninger Entsatz'},
'Hemelvaartsdag'             : {'en':'Ascension Day',
                                'de':'Christi Himmelfahrt'},
'Koninginnedag'              : {'en':"Queen's Day",
                                'de':'Königinnentag'},
'Koningsdag'                 : {'en':"King's Day",
                                'de':'Königstag'},
'Leids Ontzet'               : {'en':'Siege of Leiden',
                                'de':'Leidener Entsatz'},
'Moederdag'                  : {'en':"Mother's Day",
                                'de':'Muttertag'},
'Naturalisatiedag'           : {'en':"Naturalisation's Day",
                                'de':'Naturalisationstag'},
'Nieuwjaarsdag'              : {'en':"New Year's Day",
                                'de':'Neujahrstag'},
'Oudejaarsavond'             : {'en':"New Year's Eve",
                                'de':'Silvester'},
'Pakjesavond'                : {'en':"St. Nicholas' Eve",
                                'de':'Nikolausabend'},
'Prinsjesdag'                : {'en':"Prince's Day",
                                'de':'Prinzentag'},
'Secretaressedag'            : {'en':"Administrative Professionals' Day",
                                'de':'Sekretärinnentag'},
'Sint-Maarten'               : {'en':"St. Martin's Day",
                                'de':'Martinstag'},
'Tweede Kerstdag'            : {'en':'Boxing Day',
                                'de':'Zweiter Weihnachtsfeiertag'},
'Tweede Paasdag'             : {'en':'Easter Monday',
                                'de':'Zweiter Osterfeiertag'},
'Tweede Pinksterdag'         : {'en':'Pentecost Monday',
                                'de':'Zweiter Pfingstfeiertag'},
'Vaderdag'                   : {'en':"Father's Day",
                                'de':'Vatertag'},
'Valentijnsdag'              : {'en':"Valentine's Day",
                                'de':'Valentinstag'},
'Veteranendag'               : {'en':'Veterans Day',
                                'de':'Veteranentag'},
'Wintertijd - uur achteruit' : {'en':'Winter Time',
                                'de':'Winterzeit'},
'Zomertijd - uur vooruit'    : {'en':'Summer Time',
                                'de':'Sommerzeit'},
}

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')
calendar = open('DutchHolidays.ics', 'w', newline='\r\n')
Kalender = open('NiederlaendischUrlaub.ics', 'w', newline='\r\n')

calendar_header = open('templates/calendar-header.txt', 'r')
for line in calendar_header:
    kalender.write(line)
    calendar.write(line.replace('Nederlandse Feestdagen', translations['Nederlandse Feestdagen']['en']))
    Kalender.write(line.replace('Nederlandse Feestdagen', translations['Nederlandse Feestdagen']['de']))

# create ICS header
holiday_header = ''
event_header = open('templates/event-header.txt', 'r')
for line in event_header:
    holiday_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

# create ICS footer
holiday_footer = ''
event_footer = open('templates/event-footer.txt', 'r')
for line in event_footer:
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file), 'r')
        naam = holiday_file[:-4]
        kalender.write('{}{}\n'.format(holiday_header.strip(), naam))
        calendar.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['en']))
        Kalender.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['de']))
        # write UID and autoincrement
        kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'nl', 'seq': event_seq }.items()))))
        calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
        Kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'de', 'seq': event_seq }.items()))))
        event_seq += 1
        for line in holiday:
            kalender.write(line)
            calendar.write(line)
            Kalender.write(line)
        if 'Nieuwjaarsdag' in naam or 'Goede Vrijdag' in naam or 'Paasdag' in naam or 'Koning' in naam or 'Bevrijdinsdag' in naam or 'Hemelvaartsdag' in naam or 'Pinksterdag' in naam or 'Kerstdag' in naam:
            kalender.write(holiday_footer)
            calendar.write(holiday_footer)
            Kalender.write(holiday_footer)
        else:
            kalender.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))
            calendar.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))
            Kalender.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))

directory = 'unscripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file), 'r')
        naam = holiday_file[:-4]
        for line in holiday:
            kalender.write('{}{}\n'.format(holiday_header.strip(), naam))
            calendar.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['en']))
            Kalender.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['de']))
            # write UID and autoincrement
            kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'nl', 'seq': event_seq }.items()))))
            calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
            Kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'de', 'seq': event_seq }.items()))))
            event_seq += 1

            date = datetime.strptime(line.strip(), '%Y%m%d')
            kalender.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendar.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            Kalender.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            if naam == 'Carnaval':
                date += timedelta(days=3)
            else:
                date += timedelta(days=1)
            kalender.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendar.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            Kalender.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            if 'Nieuwjaarsdag' in naam or 'Goede Vrijdag' in naam or 'Paasdag' in naam or 'Koning' in naam or 'Bevrijdinsdag' in naam or 'Hemelvaartsdag' in naam or 'Pinksterdag' in naam or 'Kerstdag' in naam:
                kalender.write(holiday_footer)
                calendar.write(holiday_footer)
                Kalender.write(holiday_footer)
            else:
                kalender.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))
                calendar.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))
                Kalender.write(holiday_footer.replace('Public Holiday', 'Unofficial Public Holiday'))

calendar_footer = open('templates/calendar-footer.txt', 'r')
for line in calendar_footer:
    kalender.write(line)
    calendar.write(line)
    Kalender.write(line)
