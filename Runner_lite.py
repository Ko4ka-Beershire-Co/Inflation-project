# Cart imports
import gspread as gc
from oauth2client.service_account import ServiceAccountCredentials

# Parser imports
import requests
from datetime import datetime
import re
from bs4 import BeautifulSoup

# Runner imports
import os
import shutil
import importlib
import time
import datetime
from termcolor import colored

parser_location = "C://Users/Alex/PycharmProjects/Inflation-project/Parcer_folder_pipeline"
parser_list = []
k = 0


def push_value(name, i):
    ref_row = 3
    ref_col = 4
    # df to Google Sheet module ------ So this is a shitty version as it requires 2 cached files in the root directory
    # !!! email me at Alex@beershire.ru to get your access to the g-sheet !!!
    # the client_key.json, which will later be integrated as a part of utils.js or utils.py
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name('client_key.json', scope)  # Root location
    client = gc.authorize(credentials)

    spreadsheet = client.open('Inflation_project')  # this has to match the credentials

    # So here is the idea, when the function is called externally __name__ = filename (.py extension?)
    # That's why on every run the function will address the correct column via addressing REF_INDEX
    worksheet = spreadsheet.worksheet("REF_INDEX")  # Opus magnum of my Excel skills
    python_file = worksheet.find(name)  # I need R\d\dC

    # python_file = str(python_file)[6:9]  # We need row only, 2 in my example
    python_file = re.findall(r'.(.\d*C)', str(python_file), re.MULTILINE)[0]

    REF_R_coordinates = python_file + str(ref_row)  # R2C3 R%Row_number% in the sheet
    REF_R_coordinates = re.findall(r'(R\d*C\d)', str(REF_R_coordinates), re.MULTILINE)[0]
    REF_C_coordinates = python_file + str(ref_col)  # R2C4 C%Col_number% in the sheet
    if len(REF_R_coordinates) < 5:
        Rr = str(REF_R_coordinates[1:4:2])  # 23
        R1 = Rr[0:1]  # 2
        R2 = Rr[1:2]  # 3
        Cc = str(REF_C_coordinates[1:4:2])
        C1 = Cc[0:1]  # 2
        C2 = Cc[1:2]  # 3
    else:
        Rr = str(REF_R_coordinates[1:3:1]) + str(REF_R_coordinates[-1:])
        R1 = Rr[0:2]  # 2
        R2 = Rr[2:3]  # 3
        Cc = str(REF_C_coordinates[1:3:1]) + str(REF_C_coordinates[-1:])
        C1 = Cc[0:2]  # 2
        C2 = Cc[2:3]  # 4

    # Okay so we have [2, 3] for Y value that is a numeral
    # And [2, 4] For X value, which is a letter
    x = worksheet.cell(C1, C2).value  # Pen
    y = worksheet.cell(R1, R2).value  # Apple
    # I have a pen, I have an apple -> Uh! Apple pen!
    next_cell = x + y

    worksheet_2 = spreadsheet.worksheet("RAW_DATA")
    worksheet_2.update(next_cell, i)


def revolve():
    # List all Parser in the target folder
    for filename in os.listdir(parser_location):
        parser_list.append(filename)

    # Parse and push script
    for k in parser_list[:-1]:  # -1 deletes _pycache_

        # exception for readme
        if k == "readme.md":
            pass  # pass = skip

        else:
            time.sleep(3)
            # from package import name as imported
            print(colored(str(k) + '---|Running', 'green'))
            package = "Parcer_folder_pipeline." + k[:-3]
            name = "parser"

            # Very blya complicated
            imported = getattr(__import__(package, fromlist=[name]), name)
            # Make it a number
            try:
                # If I want to parse date, or some other stuff, I don't want the RegEx
                if k != 'Date.py':
                    end_value = re.sub(r'[^\d\.]', '', str(imported()), 0, re.MULTILINE)
                    push_value(str(k), float(end_value))
                    print(colored(str(k) + '---------|Success', "green"))

                else:
                    push_value(str(k), imported())
                    print(colored(str(k) + '---------|Success', "green"))

            # Some Chris Nolan Shit Happening Here
            except:
                # JIC RegEx breaks smt
                try:
                    push_value(str(k), float(imported()))
                    print(colored(str(k) + '---------|Success|---------Under-"else_statement"', "yellow"))

                except:

                    print(colored(str(k) + '---------|Error', 'red'))
                    # If Error - quick fix
                    # Take previous value from the table and copy-paste it with a highlight

                    pass


if __name__ == '__main__':
    revolve()
