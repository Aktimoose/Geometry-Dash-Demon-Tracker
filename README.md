# Geometry Dash Demon Tracker
python script to append demons input into a spreadsheet

### example sheet
[Aktimoose Demon Tracker](https://docs.google.com/spreadsheets/d/1uO9rHULB91mQE90L5cjj_YYB_CPxYk8zqd8KcgWsOq0/?gid=0)

## demontracker.py

automatically appends any demon you input into it onto a sheet with the current date.

the name of the sheet is hardcoded in Line 83 and you'll need to change that part if you wish to use it yourself.

requires requests and gspread

## demontracker - clipboard.py

demontracker - clipboard.py lets you input a demon into it and then it copies the data for that demon to the clipboard. it skips the date field.

useful for inputting data for previous demons

requires requests and pyperclip
