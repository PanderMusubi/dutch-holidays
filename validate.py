#!/usr/bin/env python3
"""Generate ICS files in Dutch and English for Dutch holidays."""

from icalendar import Calendar

# use recursive glob
for lang in ('nl', 'en', 'de', 'fr', 'es', 'it'):
    with open(f'{lang}.ics', 'rb') as file:
        try:
            Calendar.from_ical(file.read())
            print('ICS file is valid.')
        except Exception as e:
            print('Invalid ICS file:', e)
