#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
import scrape_common as sc

print('SZ')

d = sc.download('https://www.sz.ch/behoerden/information-medien/medienmitteilungen/coronavirus.html/72-416-412-1379-6948')
soup = BeautifulSoup(d, 'html.parser')
xls_url = soup.find('a', string=re.compile(r'Coronaf.lle\s*im\s*Kanton\s*Schwyz'))['href']
xls = sc.xlsdownload(xls_url)
sc.timestamp()

sheet = xls.sheet_by_index(0)
last_row = sheet.nrows - 1

date_value = sheet.cell_value(last_row, 0)
current_date = sc.xldate_as_datetime(sheet, date_value)
print('Date and time:', current_date.date().isoformat())

cases = int(sheet.cell_value(last_row, 1)) 
print('Confirmed cases:', cases)

deaths = int(sheet.cell_value(last_row, 2))
if deaths:
    print('Deaths:', deaths)

recovered = int(sheet.cell_value(last_row, 3))
if recovered:
    print('Recovered:', recovered)
