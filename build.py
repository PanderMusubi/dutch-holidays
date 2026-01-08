#!/usr/bin/env python3
"""Generate ICS files in Dutch and English for Dutch holidays."""

from datetime import datetime, timedelta, UTC
from hashlib import sha256
from os import listdir
from json import load

# pylint:disable=unspecified-encoding

utcnow = datetime.now(UTC)
TRANSLATIONS = load(open('translations.json'))

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')
calendar = open(TRANSLATIONS['NederlandseFeestdagen.ics']['en'], 'w',
                newline='\r\n')
calendrier = open(TRANSLATIONS['NederlandseFeestdagen.ics']['fr'], 'w',
                  newline='\r\n')
Kalender = open(TRANSLATIONS['NederlandseFeestdagen.ics']['de'], 'w',
                newline='\r\n')
calendario = open(TRANSLATIONS['NederlandseFeestdagen.ics']['es'], 'w',
                  newline='\r\n')
calendario_it = open(TRANSLATIONS['NederlandseFeestdagen.ics']['it'], 'w',
                     newline='\r\n')

# write calendar header
with open('templates/calendar-header.txt') as f:
    for line in f:
        kalender.write(line)
        calendar.write(line.replace('Nederlandse Feestdagen',
                                    TRANSLATIONS['Nederlandse Feestdagen']
                                    ['en']).replace('//NL', '//EN'))
        calendrier.write(line.replace('Nederlandse Feestdagen',
                                      TRANSLATIONS['Nederlandse Feestdagen']
                                      ['fr']).replace('//NL', '//FR'))
        Kalender.write(line.replace('Nederlandse Feestdagen',
                                     TRANSLATIONS['Nederlandse Feestdagen']
                                     ['de']).replace('//NL', '//DE'))
        calendario.write(line.replace('Nederlandse Feestdagen',
                                      TRANSLATIONS['Nederlandse Feestdagen']
                                      ['es']).replace('//NL', '//ES'))
        calendario_it.write(line.replace('Nederlandse Feestdagen',
                                         TRANSLATIONS['Nederlandse Feestdagen']
                                         ['it']).replace('//NL', '//IT'))

# create event header
holiday_header = ''
with open('templates/event-header.txt') as f:
    for line in f:
        holiday_header += line.replace('DTSTAMP:', 'DTSTAMP:20091231T040000Z')

# create event footer
holiday_footer = ''
with open('templates/event-footer.txt') as f:
    for line in f:
        holiday_footer += line

directory = 'scripted-holidays'
for holiday_file in sorted(listdir(directory)):
    if holiday_file.endswith(".txt"):
        holiday = open(f'{directory}/{holiday_file}')
        naam = holiday_file[:-4]

        # write event header
        kalender.write(f'{holiday_header.strip()}{naam}\n')
        calendar.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["en"]})\n')
        calendrier.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["fr"]})\n')
        Kalender.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["de"]})\n')
        calendario.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["es"]})\n')
        calendario_it.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["it"]})\n')

        datum = ''
        for line in holiday:
            if 'DTSTART;VALUE=DATE:' in line:
                datum = line.split('DTSTART;VALUE=DATE:', 1)[1].split('\n')[0]
            kalender.write(line)
            calendar.write(line)
            calendrier.write(line)
            Kalender.write(line)
            calendario.write(line)
            calendario_it.write(line)

        # write UID
        uid = sha256((naam + datum + 'nl').encode()).hexdigest()[:16]
        kalender.write(f'UID:{uid}@github.com/pandermusubi\n')
        uid = sha256((TRANSLATIONS[naam]['en'] + datum + 'en').encode()).hexdigest()[:16]
        calendar.write(f'UID:{uid}@github.com/pandermusubi\n')
        uid = sha256((TRANSLATIONS[naam]['fr'] + datum + 'fr').encode()).hexdigest()[:16]
        calendrier.write(f'UID:{uid}@github.com/pandermusubi\n')
        uid = sha256((TRANSLATIONS[naam]['de'] + datum + 'de').encode()).hexdigest()[:16]
        Kalender.write(f'UID:{uid}@github.com/pandermusubi\n')
        uid = sha256((TRANSLATIONS[naam]['es'] + datum + 'es').encode()).hexdigest()[:16]
        calendario.write(f'UID:{uid}@github.com/pandermusubi\n')
        uid = sha256((TRANSLATIONS[naam]['it'] + datum + 'it').encode()).hexdigest()[:16]
        calendario_it.write(f'UID:{uid}@github.com/pandermusubi\n')
    
        # write event URL attachment
        kalender.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
        calendar.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
        calendrier.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
        Kalender.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
        calendario.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
        calendario_it.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')

        # write event CATEGORIES
        kalender.write(f'CATEGORIES:{TRANSLATIONS[naam]["type"]}\n')
        calendar.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["en"]}\n')
        calendrier.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["fr"]}\n')
        Kalender.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["de"]}\n')
        calendario.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["es"]}\n')
        calendario_it.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["it"]}\n')

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
        holiday = open(f'{directory}/{holiday_file}')
        naam = holiday_file[:-4]
        for line in holiday:
            # write event header
            kalender.write(f'{holiday_header.strip()}{naam}\n')
            calendar.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["en"]})\n')
            calendrier.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["fr"]})\n')
            Kalender.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["de"]})\n')
            calendario.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["es"]})\n')
            calendario_it.write(f'{holiday_header.strip()}{naam} ({TRANSLATIONS[naam]["it"]})\n')

            date = datetime.strptime(line.strip(), '%Y%m%d')
            # write UID
            uid = sha256((naam + date.strftime("%Y%m%d") + 'nl').encode()).hexdigest()[:16]
            kalender.write(f'UID:{uid}@github.com/pandermusubi\n')
            uid = sha256((TRANSLATIONS[naam]['en'] + date.strftime("%Y%m%d") + 'en').encode()).hexdigest()[:16]
            calendar.write(f'UID:{uid}@github.com/pandermusubi\n')
            uid = sha256((TRANSLATIONS[naam]['fr'] + date.strftime("%Y%m%d") + 'fr').encode()).hexdigest()[:16]
            calendrier.write(f'UID:{uid}@github.com/pandermusubi\n')
            uid = sha256((TRANSLATIONS[naam]['de'] + date.strftime("%Y%m%d") + 'de').encode()).hexdigest()[:16]
            Kalender.write(f'UID:{uid}@github.com/pandermusubi\n')
            uid = sha256((TRANSLATIONS[naam]['es'] + date.strftime("%Y%m%d") + 'es').encode()).hexdigest()[:16]
            calendario.write(f'UID:{uid}@github.com/pandermusubi\n')
            uid = sha256((TRANSLATIONS[naam]['it'] + date.strftime("%Y%m%d") + 'it').encode()).hexdigest()[:16]
            calendario_it.write(f'UID:{uid}@github.com/pandermusubi\n')

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
            kalender.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
            calendar.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
            calendrier.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
            Kalender.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
            calendario.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')
            calendario_it.write(f'ATTACH:{TRANSLATIONS[naam]["url"]}\n')

            # write event CATEGORIES
            kalender.write(f'CATEGORIES:{TRANSLATIONS[naam]["type"]}\n')
            calendar.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["en"]}\n')
            calendrier.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["fr"]}\n')
            Kalender.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["de"]}\n')
            calendario.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["es"]}\n')
            calendario_it.write(f'CATEGORIES:{TRANSLATIONS[TRANSLATIONS[naam]["type"]]["it"]}\n')

            # write event footer
            kalender.write(holiday_footer)
            calendar.write(holiday_footer)
            calendrier.write(holiday_footer)
            Kalender.write(holiday_footer)
            calendario.write(holiday_footer)
            calendario_it.write(holiday_footer)

# write calendar footer
with open('templates/calendar-footer.txt') as f:
    for line in f:
        kalender.write(line)
        calendar.write(line)
        calendrier.write(line)
        Kalender.write(line)
        calendario.write(line)
        calendario_it.write(line)
