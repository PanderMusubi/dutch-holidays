#!/usr/bin/env python3
"""Generate ICS files in Dutch and English for Dutch holidays."""

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
    'pid': getpid(),
    'domain': getfqdn()
}
event_seq = 1

# translations
translations = load(open('translations.json'))  # pylint:disable=consider-using-with,unspecified-encoding

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')  # pylint:disable=consider-using-with,unspecified-encoding
calendar = open(translations['NederlandseFeestdagen.ics']['en'], 'w',  # pylint:disable=consider-using-with,unspecified-encoding
                newline='\r\n')
calendrier = open(translations['NederlandseFeestdagen.ics']['fr'], 'w',  # pylint:disable=consider-using-with,unspecified-encoding
                  newline='\r\n')
Kalender = open(translations['NederlandseFeestdagen.ics']['de'], 'w',  # pylint:disable=consider-using-with,unspecified-encoding
                newline='\r\n')
calendario = open(translations['NederlandseFeestdagen.ics']['es'], 'w',  # pylint:disable=consider-using-with,unspecified-encoding
                  newline='\r\n')
calendario_it = open(translations['NederlandseFeestdagen.ics']['it'], 'w',  # pylint:disable=consider-using-with,unspecified-encoding
                     newline='\r\n')

# write calendar header
calendar_header = open('templates/calendar-header.txt')  # pylint:disable=consider-using-with,unspecified-encoding
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
    calendario_it.write(line.replace('Nederlandse Feestdagen',
                                     translations['Nederlandse Feestdagen']
                                     ['it']))

# create event header
holiday_header = ''
event_header = open('templates/event-header.txt')  # pylint:disable=consider-using-with,unspecified-encoding
for line in event_header:
    holiday_header += line.replace('DTSTAMP:', f'DTSTAMP:{dtstamp}')

# create event footer
holiday_footer = ''
event_footer = open('templates/event-footer.txt')  # pylint:disable=consider-using-with,unspecified-encoding
for line in event_footer:
    holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open(f'{directory}/{holiday_file}')  # pylint:disable=consider-using-with,unspecified-encoding
        naam = holiday_file[:-4]

        # write event header
        kalender.write(f'{holiday_header.strip()}{naam}\n')
        calendar.write(f'{holiday_header.strip()}{naam} ({translations[naam]["en"]})\n')
        calendrier.write(f'{holiday_header.strip()}{naam} ({translations[naam]["fr"]})\n')
        Kalender.write(f'{holiday_header.strip()}{naam} ({translations[naam]["de"]})\n')
        calendario.write(f'{holiday_header.strip()}{naam} ({translations[naam]["es"]})\n')
        calendario_it.write(f'{holiday_header.strip()}{naam} ({translations[naam]["it"]})\n')

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
        calendario_it.write(uid_format % (dict(list(uid_replace_values.items()) +
                                               list({'lang': 'it',
                                                     'seq': event_seq}.items()))))
        event_seq += 1

        for line in holiday:
            kalender.write(line)
            calendar.write(line)
            calendrier.write(line)
            Kalender.write(line)
            calendario.write(line)
            calendario_it.write(line)

        # write event URL attachment
        kalender.write(f'ATTACH:{translations[naam]["url"]}\n')
        calendar.write(f'ATTACH:{translations[naam]["url"]}\n')
        calendrier.write(f'ATTACH:{translations[naam]["url"]}\n')
        Kalender.write(f'ATTACH:{translations[naam]["url"]}\n')
        calendario.write(f'ATTACH:{translations[naam]["url"]}\n')
        calendario_it.write(f'ATTACH:{translations[naam]["url"]}\n')

        # write event CATEGORIES
        kalender.write(f'CATEGORIES:{translations[naam]["type"]}\n')
        calendar.write(f'CATEGORIES:{translations[translations[naam]["type"]]["en"]}\n')
        calendrier.write(f'CATEGORIES:{translations[translations[naam]["type"]]["fr"]}\n')
        Kalender.write(f'CATEGORIES:{translations[translations[naam]["type"]]["de"]}\n')
        calendario.write(f'CATEGORIES:{translations[translations[naam]["type"]]["es"]}\n')
        calendario_it.write(f'CATEGORIES:{translations[translations[naam]["type"]]["it"]}\n')

        # write event footer
        kalender.write(holiday_footer)
        calendar.write(holiday_footer)
        calendrier.write(holiday_footer)
        Kalender.write(holiday_footer)
        calendario.write(holiday_footer)
        calendario_it.write(holiday_footer)

directory = 'unscripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open(f'{directory}/{holiday_file}')  # pylint:disable=consider-using-with,unspecified-encoding
        naam = holiday_file[:-4]
        for line in holiday:
            # write event header
            kalender.write(f'{holiday_header.strip()}{naam}\n')
            calendar.write(f'{holiday_header.strip()}{naam} ({translations[naam]["en"]})\n')
            calendrier.write(f'{holiday_header.strip()}{naam} ({translations[naam]["fr"]})\n')
            Kalender.write(f'{holiday_header.strip()}{naam} ({translations[naam]["de"]})\n')
            calendario.write(f'{holiday_header.strip()}{naam} ({translations[naam]["es"]})\n')
            calendario_it.write(f'{holiday_header.strip()}{naam} ({translations[naam]["it"]})\n')

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
            calendario_it.write(uid_format % (dict(
                list(uid_replace_values.items()) +
                list({'lang': 'it', 'seq': event_seq}.items()))))
            event_seq += 1

            date = datetime.strptime(line.strip(), '%Y%m%d')
            kalender.write(f'DTSTART;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendar.write(f'DTSTART;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendrier.write(f'DTSTART;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            Kalender.write(f'DTSTART;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendario.write(f'DTSTART;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendario_it.write(f'DTSTART;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            if naam == 'Carnaval':
                date += timedelta(days=3)
            else:
                date += timedelta(days=1)
            kalender.write(f'DTEND;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendar.write(f'DTEND;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendrier.write(f'DTEND;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            Kalender.write(f'DTEND;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendario.write(f'DTEND;VALUE=DATE:{date.strftime("%Y%m%d")}\n')
            calendario_it.write(f'DTEND;VALUE=DATE:{date.strftime("%Y%m%d")}\n')

            # write event URL attachment
            kalender.write(f'ATTACH:{translations[naam]["url"]}\n')
            calendar.write(f'ATTACH:{translations[naam]["url"]}\n')
            calendrier.write(f'ATTACH:{translations[naam]["url"]}\n')
            Kalender.write(f'ATTACH:{translations[naam]["url"]}\n')
            calendario.write(f'ATTACH:{translations[naam]["url"]}\n')
            calendario_it.write(f'ATTACH:{translations[naam]["url"]}\n')

            # write event CATEGORIES
            kalender.write(f'CATEGORIES:{translations[naam]["type"]}\n')
            calendar.write(f'CATEGORIES:{translations[translations[naam]["type"]]["en"]}\n')
            calendrier.write(f'CATEGORIES:{translations[translations[naam]["type"]]["fr"]}\n')
            Kalender.write(f'CATEGORIES:{translations[translations[naam]["type"]]["de"]}\n')
            calendario.write(f'CATEGORIES:{translations[translations[naam]["type"]]["es"]}\n')
            calendario_it.write(f'CATEGORIES:{translations[translations[naam]["type"]]["it"]}\n')

            # write event footer
            kalender.write(holiday_footer)
            calendar.write(holiday_footer)
            calendrier.write(holiday_footer)
            Kalender.write(holiday_footer)
            calendario.write(holiday_footer)
            calendario_it.write(holiday_footer)

# write calendar footer
calendar_footer = open('templates/calendar-footer.txt')  # pylint:disable=consider-using-with,unspecified-encoding
for line in calendar_footer:
    kalender.write(line)
    calendar.write(line)
    calendrier.write(line)
    Kalender.write(line)
    calendario.write(line)
    calendario_it.write(line)
