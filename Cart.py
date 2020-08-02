import pandas as pd
import gspread as gc
from oauth2client.service_account import ServiceAccountCredentials

i = '1'

#df to Google Sheet module ------ So this is a shitty version as it requires 2 cached files in the root directory
# !!! email me at Alex@beershire.ru to get your access to the g-sheet !!!
# the client_key.json, which will later be integrated as a part of utils.js or utils.py
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_key.json', scope)  # Root location
client = gc.authorize(credentials)

spreadsheet = client.open('Beershire_stock_parser')  # this has to match the credentials

worksheet = spreadsheet.worksheet("TEMP")

worksheet.update('B2', i)
