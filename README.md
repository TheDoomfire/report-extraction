# Report Extraction
For extraction data from a .PDF like [They Do](https://www.pdftoexcel.com/) but remove useless text? Only "real" tables

## Installations

Create a venv `python -m venv .venv` //Name the folder whatever you want.

Activate it - Win: `source .venv/Scripts/activate` Mac: `source .venv/bin/activate`

### Requirements

`pip freeze > requirements.txt` - Create the requirements.txt
`pip install -r requirements.txt` - Installs it.

### Create a .exe file

`pyinstaller --icon=icon.ico main.py --onefile --noconsole`

1. **--noconsole** removes the command window
1. **--onefile** makes it only one file compared to several
1. **--icon=** app icon