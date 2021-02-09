#!/usr/bin/env python3
"""
Generate ICS files in Dutch and English for Dutch holidays.

Name		process-holidays.py
Author		Pander <pander@users.sourceforge.net>
License		Public domain
"""

from datetime import datetime, timedelta
from os import getpid, listdir
from socket import getfqdn
from json import load

# date and time
utcnow = datetime.utcnow()
dtstamp = utcnow.strftime('%Y%m%dT%H%M%SZ')

# event UID
uid_format = 'UID:%(date)s-%(pid)d-%(seq)04d-%(lang)s@%(domain)s\n'
uid_replace_values = {
    'date': dtstamp,
    'pid':  getpid(),
    'domain': getfqdn()
}
event_seq = 1

# translations
translations = load(open('translations.json'))

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')
calendar = open(translations['NederlandseFeestdagen.ics']['en'], 'w',
                newline='\r\n')
calendrier = open(translations['NederlandseFeestdagen.ics']['fr'], 'w',
                  newline='\r\n')
Kalender = open(translations['NederlandseFeestdagen.ics']['de'], 'w',
                newline='\r\n')

# write calendar header
calendar_header = open('templates/calendar-header.txt')
for line in calendar_header:
    kalender.write(line)
    calendar.write(line.replace('Nederlandse Feestdagen',
                                translations['Nederlandse Feestdagen']
                                ['en']))
    calendrier.write(line.replace('Nederlandse Feestdagen',
                                  translations['Nederlandse Feestdagen']
                                  ['fr']))
    Kalender.write(line.replace('Nederlandse Feestdagen',
                                translations['Nederlandse Feestdagen']
                                ['de']))

# create event header
holiday_header = ''
event_header = open('templates/event-header.txt')
for line in event_header:
    holiday_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

# create event footer
holiday_footer = ''
event_footer = open('templates/event-footer.txt')
for line in event_footer:
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file))
        naam = holiday_file[:-4]

        # write event header
        kalender.write('{}{}\n'.format(holiday_header.strip(), naam))
        calendar.write('{}{} ({})\n'.format(holiday_header.strip(),
                                            naam, translations[naam]['en']))
        calendrier.write('{}{} ({})\n'.format(holiday_header.strip(),
                                              naam, translations[naam]['fr']))
        Kalender.write('{}{} ({})\n'.format(holiday_header.strip(),
                                            naam, translations[naam]['de']))

        # write event UID and autoincrement
        kalender.write(uid_format % (dict(list(uid_replace_values.items()) +
                                          list({'lang': 'nl',
                                                'seq': event_seq}.items())
                                          )))
        calendar.write(uid_format % (dict(list(uid_replace_values.items()) +
                                          list({'lang': 'en',
                                                'seq': event_seq}.items())
                                          )))
        calendrier.write(uid_format % (dict(list(uid_replace_values.items()) +
                                            list({'lang': 'fr',
                                                  'seq': event_seq}.items())
                                            )))
        Kalender.write(uid_format % (dict(list(uid_replace_values.items()) +
                                          list({'lang': 'de',
                                                'seq': event_seq}.items()))))
        event_seq += 1

        for line in holiday:
            kalender.write(line)
            calendar.write(line)
            Kalender.write(line)

        # write event URL attachment
        kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
        calendar.write('ATTACH:{}\n'.format(translations[naam]['url']))
        Kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))

        # write event CATEGORIES
        kalender.write('CATEGORIES:{}\n'.
                       format(translations[naam]['type']))
        calendar.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['en']))
        calendrier.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['fr']))
        Kalender.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['de']))

        # write event footer
        kalender.write(holiday_footer)
        calendar.write(holiday_footer)
        Kalender.write(holiday_footer)

directory = 'unscripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file))
        naam = holiday_file[:-4]
        for line in holiday:
            # write event header
            kalender.write('{}{}\n'.format(holiday_header.strip(), naam))
            calendar.write('{}{} ({})\n'.format(
                           holiday_header.strip(), naam,
                           translations[naam]['en']))
            calendrier.write('{}{} ({})\n'.format(
                             holiday_header.strip(), naam,
                             translations[naam]['fr']))
            Kalender.write('{}{} ({})\n'.format(
                        holiday_header.strip(), naam,
                        translations[naam]['de']))

            # write event UID and autoincrement
            kalender.write(uid_format % (dict(
                list(uid_replace_values.items()) +
                list({'lang': 'nl', 'seq': event_seq}.items()))))
            calendar.write(uid_format % (dict(
                list(uid_replace_values.items()) +
                list({'lang': 'en', 'seq': event_seq}.items()))))
            calendrier.write(uid_format % (dict(
                list(uid_replace_values.items()) +
                list({'lang': 'fr', 'seq': event_seq}.items()))))
            Kalender.write(uid_format % (dict(
                list(uid_replace_values.items()) +
                list({'lang': 'de', 'seq': event_seq}.items()))))
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

            # write event URL attachment
            kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
            calendar.write('ATTACH:{}\n'.format(translations[naam]['url']))
            Kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))

            # write event CATEGORIES
            kalender.write('CATEGORIES:{}\n'.format(
                translations[naam]['type']))
            calendar.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['en']))
            calendrier.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['fr']))
            Kalender.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['de']))

            # write event footer
            kalender.write(holiday_footer)
            calendar.write(holiday_footer)
            Kalender.write(holiday_footer)

# write calendar footer
calendar_footer = open('templates/calendar-footer.txt')
for line in calendar_footer:
    kalender.write(line)
    calendar.write(line)
    calendrier.write(line)
    Kalender.write(line)
