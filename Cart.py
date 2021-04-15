import gspread as gc
from oauth2client.service_account import ServiceAccountCredentials
import re


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

    #python_file = str(python_file)[6:9]  # We need row only, 2 in my example
    python_file = re.findall(r'.(.\d*C)', str(python_file), re.MULTILINE)[0]


    REF_R_coordinates = python_file + str(ref_row)  # R2C3 R%Row_number% in the sheet
    REF_R_coordinates = re.findall(r'(R\d*C\d)', str(REF_R_coordinates), re.MULTILINE)[0]
    REF_C_coordinates = python_file + str(ref_col)  # R2C4 C%Col_number% in the sheet
    print(REF_C_coordinates)
    if len(REF_R_coordinates) < 5:
        Rr = str(REF_R_coordinates[1:4:2])  # 23
        R1 = Rr[0:1]  # 2
        R2 = Rr[1:2]  # 3
        Cc = str(REF_C_coordinates[1:4:2])
        C1 = Cc[0:1]  # 2
        C2 = Cc[1:2]  # 3
    else:
        Rr = str(REF_R_coordinates[1:3:1])+str(REF_R_coordinates[-1:])
        R1 = Rr[0:2]  # 2
        R2 = Rr[2:3]  # 3
        Cc = str(REF_C_coordinates[1:3:1])+str(REF_C_coordinates[-1:])
        C1 = Cc[0:2]  # 2
        C2 = Cc[2:3]  # 4


    # Okay so we have [2, 3] for Y value that is a numeral
    # And [2, 4] For X value, which is a letter
    x = worksheet.cell(C1, C2).value  # Pen
    y = worksheet.cell(R1, R2).value  # Apple
    # I have a pen, I have an apple -> Uh! Apple pen!
    next_cell = x + y
    print(next_cell)

    worksheet_2 = spreadsheet.worksheet("RAW_DATA")
    worksheet_2.update(next_cell, i)


if __name__ == "__main__":
    push_value('Asparagus.py', 2)

