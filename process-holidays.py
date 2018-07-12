#!/usr/bin/env python3
"""
Name		process-holidays.py
Description	Generate ICS files in Dutch and English for Dutch holidays
Author		Pander <pander@users.sourceforge.net>
License		Public domain

0.7 2018-07-12	Pander <pander@users.sourceforge.net>
Added French translation

0.6 2016-11-??	Pander <pander@users.sourceforge.net>
Added categories and URLs

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
                                'fr':'Jours fériés aux Pays Bas',
                                'de':'Niederländische Feiertage'},
'NederlandseFeestdagen.ics'  : {'en':'DutchHolidays.ics',
                                'fr':'JoursFeriesAuxPaysBas.ics',
                                'de':'NiederlaendischeFeiertage.ics'},
'Nationale Feestdag'         : {'en':'National Holiday',
                                'fr':'Fête nationale',
                                'de':'Nationalfeiertag'},
'Algemeen Erkende Feestdag'  : {'en':'Public Holiday',
                                'fr':'Jour férié',
                                'de':'Allgemein anerkannte Feiertag'},
'Feestdag'                   : {'en':'Holiday',
                                'fr':'Fête',
                                'de':'Feiertag'},
'Feestavond'                 : {'en':'Evening Celebration',
                                'fr':'Réveillon',
                                'de':'Abendfeier'},
'Lokale Feestdag'            : {'en':'Local Holiday',
                                'fr':'Fête régionale',
                                'de':'Localer Feiertag'},
'Infrastructuurwijziging'    : {'en':'Infrastructure Change',
                                'fr':'Modifications d’infrastructure',
                                'de':'Infrastrukturanpassung'},

'Alkmaars Ontzet'            : {'type':'Lokale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Alkmaars_Ontzet',
                                'en':'Siege of Alkmaar',
                                'fr':'Siège d’Alkmaar',
                                'de':'Alkmaarder Entsatz'},
'Bevrijdingsdag'             : {'type':'Nationale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Bevrijdingsdag',
                                'en':'Liberation Day',
                                'fr':'Libération',
                                'de':'Befreiungstag'},
'Carnaval'                   : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Carnaval',
                                'en':'Carnival',
                                'fr':'Carnaval',
                                'de':'Karneval'},
'Dag van de Arbeid'          : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Dag_van_de_Arbeid',
                                'en':'May Day',
                                'fr':'Fête du Travail',
                                'de':'Tag der Arbeit'},
'Dierendag'                  : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Dierendag',
                                'en':'Animal Day',
                                'fr':'Journée mondiale des animaux',
                                'de':'Welttierschutztag'},
'Dodenherdenking'            : {'type':'Feestavond',
                                'url':'https://nl.wikipedia.org/wiki/Nationale_Dodenherdenking',
                                'en':'Remembrance of the Dead',
                                'fr':'Journée nationale du souvenir',
                                'de':'Volkstrauertag'},
'Driekoningen'               : {'type':'Lokale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Driekoningen',
                                'en':'Epiphany',
                                'fr':'Epiphanie',
                                'de':'Dreikönigstag'},
'Eerste Kerstdag'            : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Eerste_kerstdag',
                                'en':'Christmas Day',
                                'fr':'Noël',
                                'de':'Erster Weihnachtsfeiertag'},
'Eerste Paasdag'             : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Eerste_Paasdag',
                                'en':'Easter Sunday',
                                'fr':'Pâques',
                                'de':'Erster Osterfeiertag'},
'Eerste Pinksterdag'         : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Eerste_Pinksterdag',
                                'en':'Pentecost Sunday',
                                'fr':'Pentecôte',
                                'de':'Erster Pfingstfeiertag'},
'Goede Vrijdag'              : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Goede_Vrijdag',
                                'en':'Good Friday',
                                'fr':'Vendredi Saint',
                                'de':'Karfreitag'},
'Gronings Ontzet'            : {'type':'Lokale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Gronings_Ontzet',
                                'en':'Siege of Groningen',
                                'fr':'Siège de Groningue',
                                'de':'Groninger Entsatz'},
'Halloween'                  : {'type':'Feestavond',
                                'url':'https://nl.wikipedia.org/wiki/Halloween',
                                'en':'Halloween',
                                'fr':'Halloween',
                                'de':'Halloween'},
'Hemelvaartsdag'             : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Hemelvaartsdag',
                                'en':'Ascension Day',
                                'fr':'Ascension',
                                'de':'Christi Himmelfahrt'},
'Inname van Den Briel'       : {'type':'Lokale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Inname_van_Den_Briel',
                                'en':'Capture of Brielle',
                                'fr':'Prise de La Brielle',
                                'de':'Einname van Den Briel'},
'Kerstavond'                 : {'type':'Feestavond',
                                'url':'https://nl.wikipedia.org/wiki/Kerstavond',
                                'en':'Christmas Eve',
                                'fr':'Réveillon de Noël',
                                'de':'Heiliger Abend'},
'Ketikoti'                   : {'type':'Lokale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Ketikoti',
                                'en':'Ketikoti – Abolition of Slavery',
                                'fr':'Ketikoti – Abolition de l’esclavage',
                                'de':'Ketikoti – Abschaffung der Sklaverei'},
'Koninginnedag'              : {'type':'Nationale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Koninginnedag',
                                'en':"Queen's Day",
                                'fr':'Fête de la Reine',
                                'de':'Königinnentag'},
'Koningsdag'                 : {'type':'Nationale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Koningsdag_(Nederland)',
                                'en':"King's Day",
                                'fr':'Fête du Roi',
                                'de':'Königstag'},
'Leids Ontzet'               : {'type':'Lokale Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Leids_Ontzet',
                                'en':'Siege of Leiden',
                                'fr':'Siège de Leyde',
                                'de':'Leidener Entsatz'},
'Moederdag'                  : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Moederdag',
                                'en':"Mother's Day",
                                'fr':'Fête des mères',
                                'de':'Muttertag'},
'Naturalisatiedag'           : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Naturalisatiedag',
                                'en':"Naturalisation's Day",
                                'fr':'Journée de la naturalisation',
                                'de':'Naturalisationstag'},
'Nieuwjaarsdag'              : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Nieuwjaarsdag',
                                'en':"New Year's Day",
                                'fr':'Jour de l’an',
                                'de':'Neujahrstag'},
'Oudejaarsavond'             : {'type':'Feestavond',
                                'url':'https://nl.wikipedia.org/wiki/Oudejaarsavond',
                                'en':"New Year's Eve",
                                'fr':'Réveillon de la Saint-Sylvestre',
                                'de':'Silvester'},
'Prinsjesdag'                : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Prinsjesdag',
                                'en':"Prince's Day",
                                'fr':'Jour des petits princes',
                                'de':'Prinzentag'},
'Secretaressedag'            : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Secretaressedag',
                                'en':"Administrative Professionals' Day",
                                'fr':'Fête des secrétaires',
                                'de':'Sekretärinnentag'},
'Sinterklaasavond'           : {'type':'Feestavond',
                                'url':'https://nl.wikipedia.org/wiki/Oudejaarsavond',
                                'en':"St. Nicholas' Eve",
                                'fr':'Réveillon de la Saint Nicolas',
                                'de':'Nikolausabend'},
'Sint-Maarten'               : {'type':'Feestavond',
                                'url':'https://nl.wikipedia.org/wiki/Sint-Maarten_(feest)',
                                'en':"St. Martin's Day",
                                'fr':'Saint Martin',
                                'de':'Martinstag'},
'Tweede Kerstdag'            : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Tweede_kerstdag',
                                'en':'Boxing Day',
                                'fr':'Lendemain de Noël',
                                'de':'Zweiter Weihnachtsfeiertag'},
'Tweede Paasdag'             : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Tweede_Paasdag',
                                'en':'Easter Monday',
                                'fr':'Lundi de Pâques',
                                'de':'Zweiter Osterfeiertag'},
'Tweede Pinksterdag'         : {'type':'Algemeen Erkende Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Tweede_Pinksterdag',
                                'en':'Pentecost Monday',
                                'fr':'Lundi de Pentecôte',
                                'de':'Zweiter Pfingstfeiertag'},
'Vaderdag'                   : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Vaderdag',
                                'en':"Father's Day",
                                'fr':'Fête des pères',
                                'de':'Vatertag'},
'Valentijnsdag'              : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Valentijnsdag',
                                'en':"Valentine's Day",
                                'fr':'Saint Valentin',
                                'de':'Valentinstag'},
'Veteranendag'               : {'type':'Feestdag',
                                'url':'https://nl.wikipedia.org/wiki/Nederlandse_Veteranendag',
                                'en':'Veterans Day',
                                'fr':'Journée des anciens combattants',
                                'de':'Veteranentag'},
'Wintertijd - uur achteruit' : {'type':'Infrastructuurwijziging',
                                'url':'https://nl.wikipedia.org/wiki/Zomertijd', # is correct url
                                'en':'Winter Time',
                                'fr':'Heure d’hiver',
                                'de':'Winterzeit'},
'Zomertijd - uur vooruit'    : {'type':'Infrastructuurwijziging',
                                'url':'https://nl.wikipedia.org/wiki/Zomertijd',
                                'en':'Summer Time',
                                'fr':'Heure d’été',
                                'de':'Sommerzeit'},
}

kalender = open('NederlandseFeestdagen.ics', 'w', newline='\r\n')
calendar = open(translations['NederlandseFeestdagen.ics']['en'], 'w', newline='\r\n')
calendrier = open(translations['NederlandseFeestdagen.ics']['fr'], 'w', newline='\r\n')
Kalender = open(translations['NederlandseFeestdagen.ics']['de'], 'w', newline='\r\n')

# write calendar header
calendar_header = open('templates/calendar-header.txt')
for line in calendar_header:
    kalender.write(line)
    calendar.write(line.replace('Nederlandse Feestdagen', translations['Nederlandse Feestdagen']['en']))
    calendrier.write(line.replace('Nederlandse Feestdagen', translations['Nederlandse Feestdagen']['fr']))
    Kalender.write(line.replace('Nederlandse Feestdagen', translations['Nederlandse Feestdagen']['de']))

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
        calendar.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['en']))
        calendrier.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['fr']))
        Kalender.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['de']))

        # write event UID and autoincrement
        kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'nl', 'seq': event_seq }.items()))))
        calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
        calendrier.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'fr', 'seq': event_seq }.items()))))
        Kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'de', 'seq': event_seq }.items()))))
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
        kalender.write('CATEGORIES:{}\n'.format(translations[naam]['type']))
        calendar.write('CATEGORIES:{}\n'.format(translations[translations[naam]['type']]['en']))
        calendrier.write('CATEGORIES:{}\n'.format(translations[translations[naam]['type']]['fr']))
        Kalender.write('CATEGORIES:{}\n'.format(translations[translations[naam]['type']]['de']))

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
            calendar.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['en']))
            calendrier.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['fr']))
            Kalender.write('{}{} ({})\n'.format(holiday_header.strip(), naam, translations[naam]['de']))

            # write event UID and autoincrement
            kalender.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'nl', 'seq': event_seq }.items()))))
            calendar.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'en', 'seq': event_seq }.items()))))
            calendrier.write(uid_format % (dict(list(uid_replace_values.items()) + list({ 'lang': 'fr', 'seq': event_seq }.items()))))
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

            # write event URL attachment
            kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))
            calendar.write('ATTACH:{}\n'.format(translations[naam]['url']))
            Kalender.write('ATTACH:{}\n'.format(translations[naam]['url']))

            # write event CATEGORIES
            kalender.write('CATEGORIES:{}\n'.format(translations[naam]['type']))
            calendar.write('CATEGORIES:{}\n'.format(translations[translations[naam]['type']]['en']))
            calendrier.write('CATEGORIES:{}\n'.format(translations[translations[naam]['type']]['fr']))
            Kalender.write('CATEGORIES:{}\n'.format(translations[translations[naam]['type']]['de']))

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
