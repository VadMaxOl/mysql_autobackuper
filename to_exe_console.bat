pyinstaller --icon=icon.ico --workpath="%cd%" --paths="%cd%" --distpath=dist\ main.py --add-data mysqldump:mysqldump --contents-directory="."