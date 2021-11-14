#!/usr/bin/env python3
'''Generate ICS files in Dutch and English for Dutch holidays.'''

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
translations = load(open('translations.json'))  # pylint:disable=consider-using-with

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')  # pylint:disable=consider-using-with
calendar = open(translations['NederlandseFeestdagen.ics']['en'], 'w',  # pylint:disable=consider-using-with
                newline='\r\n')
calendrier = open(translations['NederlandseFeestdagen.ics']['fr'], 'w',  # pylint:disable=consider-using-with
                  newline='\r\n')
Kalender = open(translations['NederlandseFeestdagen.ics']['de'], 'w',  # pylint:disable=consider-using-with
                newline='\r\n')
calendario = open(translations['NederlandseFeestdagen.ics']['es'], 'w',  # pylint:disable=consider-using-with
                  newline='\r\n')

# write calendar header
calendar_header = open('templates/calendar-header.txt')  # pylint:disable=consider-using-with
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
    calendario.write(line.replace('Nederlandse Feestdagen',
                                translations['Nederlandse Feestdagen']
                                ['es']))

# create event header
holiday_header = ''
event_header = open('templates/event-header.txt')  # pylint:disable=consider-using-with
for line in event_header:
    holiday_header += line.replace('DTSTAMP:', 'DTSTAMP:{}'.format(dtstamp))

# create event footer
holiday_footer = ''
event_footer = open('templates/event-footer.txt')  # pylint:disable=consider-using-with
for line in event_footer:
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file))  # pylint:disable=consider-using-with
        naam = holiday_file[:-4]

        # write event header
        kalender.write('{}{}\n'.format(holiday_header.strip(), naam))
        calendar.write('{}{} ({})\n'.format(holiday_header.strip(),
                                            naam, translations[naam]['en']))
        calendrier.write('{}{} ({})\n'.format(holiday_header.strip(),
                                              naam, translations[naam]['fr']))
        Kalender.write('{}{} ({})\n'.format(holiday_header.strip(),
                                            naam, translations[naam]['de']))
        calendario.write('{}{} ({})\n'.format(holiday_header.strip(),
                                              naam, translations[naam]['es']))

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
        calendario.write(uid_format % (dict(list(uid_replace_values.items()) +
                                            list({'lang': 'es',
                                                  'seq': event_seq}.items()))))
        event_seq += 1

        for line in holiday:
            kalender.write(line)
            calendar.write(line)
            calendrier.write(line)
            Kalender.write(line)
            calendario.write(line)

        # write event URL attachment
        kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
        calendar.write('ATTACH:{}\n'.format(translations[naam]['url']))
        calendrier.write('ATTACH:{}\n'.format(translations[naam]['url']))
        Kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
        calendario.write('ATTACH:{}\n'.format(translations[naam]['url']))

        # write event CATEGORIES
        kalender.write('CATEGORIES:{}\n'.
                       format(translations[naam]['type']))
        calendar.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['en']))
        calendrier.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['fr']))
        Kalender.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['de']))
        calendario.write('CATEGORIES:{}\n'.format(
            translations[translations[naam]['type']]['es']))

        # write event footer
        kalender.write(holiday_footer)
        calendar.write(holiday_footer)
        calendrier.write(holiday_footer)
        Kalender.write(holiday_footer)
        calendario.write(holiday_footer)

directory = 'unscripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open('{}/{}'.format(directory, holiday_file))  # pylint:disable=consider-using-with
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
            calendario.write('{}{} ({})\n'.format(
                        holiday_header.strip(), naam,
                        translations[naam]['es']))

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
            calendario.write(uid_format % (dict(
                list(uid_replace_values.items()) +
                list({'lang': 'es', 'seq': event_seq}.items()))))
            event_seq += 1

            date = datetime.strptime(line.strip(), '%Y%m%d')
            kalender.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendar.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendrier.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            Kalender.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendario.write('DTSTART;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            if naam == 'Carnaval':
                date += timedelta(days=3)
            else:
                date += timedelta(days=1)
            kalender.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendar.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendrier.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            Kalender.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')
            calendario.write('DTEND;VALUE=DATE:'+date.strftime('%Y%m%d')+'\n')

            # write event URL attachment
            kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
            calendar.write('ATTACH:{}\n'.format(translations[naam]['url']))
            calendrier.write('ATTACH:{}\n'.format(translations[naam]['url']))
            Kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
            calendario.write('ATTACH:{}\n'.format(translations[naam]['url']))

            # write event CATEGORIES
            kalender.write('CATEGORIES:{}\n'.format(
                translations[naam]['type']))
            calendar.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['en']))
            calendrier.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['fr']))
            Kalender.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['de']))
            calendario.write('CATEGORIES:{}\n'.format(
                translations[translations[naam]['type']]['es']))

            # write event footer
            kalender.write(holiday_footer)
            calendar.write(holiday_footer)
            calendrier.write(holiday_footer)
            Kalender.write(holiday_footer)
            calendario.write(holiday_footer)

# write calendar footer
calendar_footer = open('templates/calendar-footer.txt')  # pylint:disable=consider-using-with
for line in calendar_footer:
    kalender.write(line)
    calendar.write(line)
    calendrier.write(line)
    Kalender.write(line)
    calendario.write(line)
