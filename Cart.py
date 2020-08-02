import gspread as gc
from oauth2client.service_account import ServiceAccountCredentials

i = 'Oh, hi Mark!'

__name__ = 'Hookers.py'


def push_value():
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

    worksheet = spreadsheet.worksheet("REF_INDEX")
    python_file = worksheet.find(__name__)
    python_file = str(python_file)[6:9]

    REF_R_coordinates = python_file + str(ref_row)  # R2C3
    REF_C_coordinates = python_file + str(ref_col)  # R2C4

    Rr = str(REF_R_coordinates[1:4:2])  # 23
    R1 = Rr[0:1]  # 2
    R2 = Rr[1:2]  # 3
    Cc = REF_C_coordinates[1:4:2]  # 24
    C1 = Cc[0:1]  # 2
    C2 = Cc[1:2]  # 4

    y = worksheet.cell(R1, R2).value
    x = worksheet.cell(C1, C2).value

    next_cell = x + y
    print(next_cell)


push_value()
