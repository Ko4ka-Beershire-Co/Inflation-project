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

parser_location = "C://Users/Alex/Desktop/Python/Inflation/Inflation-project-master/Parcer_folder_pipeline"
parser_list = []
k = 0

# List all Parser in the target folder
for filename in os.listdir(parser_location):
    parser_list.append(filename)

print(parser_list)
# Parse and push script
for k in parser_list[:-1]:  # -1 deletes _pycache_
    # from package import name as imported
    package = "Parcer_folder_pipeline."+k[:-3]
    name = "parser"
    # BLYAAAAA
    imported = getattr(__import__(package, fromlist=[name]), name)
    print(str(k))
    print(imported())

