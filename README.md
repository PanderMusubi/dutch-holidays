Dutch Holidays
==============


Introduction
------------

This project offers an overview of Dutch holidays (Nederlandse feestdagen) from 2010 until the year 2050. The file called [NederlandseFeestdagen.ics](https://raw.githubusercontent.com/PanderMusubi/dutch-holidays/master/NederlandseFeestdagen.ics) contains information only in Dutch. In the file [DutchHolidays.ics](https://raw.githubusercontent.com/PanderMusubi/dutch-holidays/master/DutchHolidays.ics), is the same information in Dutch available but an English translation is added.

The reason in the latter version for using the Dutch names first and the translation in brackets is that not all holidays can be unambiguously translated or do not exist in the English speaking world or do exist but with a different meaning or with a different date. Examples that are prone for confusion are Liberation Day, Mothers' Day, Fathers' Day, Veterans Day etcetera.


Scope
-----

Public holidays in the Netherlands can be official or non-official, can be free from work or not, can be national, regional or local and can be religious. This makes it not an easy task to select which public holidays to include and which not. Therefore the selection offered here is based upon the following criteria.

All holidays in the Netherlands which effect office hours. This can result in total closure of a business or people leaving early. Subsequently this can effect (part of) the country's infrastructure. The goal is to make people aware about the risk of planning events on or near those days. People, businesses and public services are probably not available as usual.

Perhaps you do not celibate certain religious holidays but your family, friends, colleges, suppliers or customers do. Next to making you aware of planning risks, this calendar of course also indicates when you might have days off.

School holidays are omitted because they differ throughout the country, are dependent on the level of education and are not planned many years in advance. Most businesses in the Netherlands operate normally during school holidays.

Official Dutch public holidays here are of calendar category Public Holiday. All other holidays have a calendar category called Unofficial Public Holiday. Whether or not this constitutes a free day is entirely up to the line of work. With the exception of Liberation Day, all of category Public Holiday usually result in a day off.


Usage
-----

The calendars provided here are in iCalendar or ICS format. Calendar software that can display these holiday calendars are:
* for OS-X, Windows and Linux: [Mozilla Thunderbird](https://www.mozilla.org/thunderbird/)
* web-based and indirectly on Android too: [Google Calendar](https://google.com/calendar)
* for Android only: ICSdroid from [Google Play](https://play.google.com/store/apps/details?id=at.bitfire.icsdroid) or [F-Droid](https://f-droid.org/repository/browse/?fdfilter=calendar&fdid=at.bitfire.icsdroid)
* for Android only: CalDAV-Sync from [Google Play](https://play.google.com/store/apps/details?id=org.dmfs.caldav.lib) and soon on F-Droid too
* for OS-X only: [Calendar](https://www.apple.com/osx/apps/#calendar)
* for iOS only: [iCloud Calendar](https://www.apple.com/icloud/#ccm)
* for Windows only: [Microsoft Outlook](https://products.office.com/outlook)
* web-based: [Microsoft Outlook.com](https://outlook.com)

See also this [list of applications with iCalendar support](https://en.wikipedia.org/wiki/List_of_applications_with_iCalendar_support) on Wikipedia, with many more native calendar clients and web-based systems such as ownCloud. Please note that many CMS software support displaying ICS calendars.

[![example](example.png?raw=true)](https://raw.githubusercontent.com/PanderMusubi/dutch-holidays/master/example-mobile.png)

[![example mobile](example-mobile.png?raw=true | width=540)](https://raw.githubusercontent.com/PanderMusubi/dutch-holidays/master/example-mobile.png)

Most calendar software can show these Dutch holidays to a color of your choice. Also in some software, a distinction in colour can be configured according to the calendar categories `Public Holiday` and `Unofficial Public Holiday`.

Warning: Please, do **not** import these ICS files into your calendar as they will be added only once and never get updated. Add these calendars as a shared (read-only) network calendar. These calendars do not need frequent updates, however, sometimes bugs are fixed, future years are added or holidays change in date or in name. See for example the transition from Queen's Day to King's Day, that also got another date. Most software will have a maximum update frequency of once a week, which is fine for these calendars. Syncing should also configured to take place only from server to client, computer or phone.

Dutch version
-------------

The calendar with Dutch Holidays in Dutch can be found at:
* https://raw.github.com/PanderMusubi/dutch-holidays/master/NederlandseFeestdagen.ics hosted by [GitHub](https://github.com/PanderMusubi/dutch-holidays)
* https://www.mozilla.org/media/caldata/DutchHolidays.ics hosted by [Mozilla](https://www.mozilla.org/en-US/projects/calendar/holidays/)


English version
---------------

The calendar with Dutch Holidays in English (with Dutch translation where needed) can be found at:
* https://raw.github.com/PanderMusubi/dutch-holidays/master/DutchHolidays.ics hosted by [GitHub](https://github.com/PanderMusubi/dutch-holidays)
* https://www.mozilla.org/media/caldata/DutchHolidaysEnglish.ics hosted by [Mozilla](https://www.mozilla.org/en-US/projects/calendar/holidays/)


Maintenance
-----------

The files are generated from the directories `scripted-holidays`, `unscripted-holidays` and `templates` by running  `generate.sh`. That will call `process-holidays.py` and will subsequently several essential conversions on `*.ics` and reporting in `names-used-*.txt`.

Calendars that have been generated can be validated by:
* http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fdutch-holidays%2Fmaster%2FNederlandseFeestdagen.ics
* http://severinghaus.org/projects/icv/?url=https%3A%2F%2Fraw.githubusercontent.com%2FPanderMusubi%2Fdutch-holidays%2Fmaster%2FDutchHolidays.ics
