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

# Multithreading
import multiprocessing
import time

parser_location = "C://Users/Alex/Desktop/Python/Inflation/Inflation-project-master/Parcer_folder_pipeline"
parser_list = []
k = 0

#

# List all Parser in the target folder
for filename in os.listdir(parser_location):
    parser_list.append(filename)

# Parse and push script
for k in parser_list[:-1]:  # -1 deletes _pycache_
    # from package import name as imported
    package = "Parcer_folder_pipeline." + k[:-3]
    name = "parser"

    # Very blya complicated
    imported = getattr(__import__(package, fromlist=[name]), name)
    try:
        if __name__ == '__main__':
            # kick-in multithreading
            thread = multiprocessing.Process(target=print(imported()))
            thread.start()
            # Timeout
            thread.join(20)
            # What it time > X(join)
            if thread.is_alive():
                print('Timeout')
                thread.terminate()  # Soft
                # thread.kill()  # Hard
                # Finish
                thread.join()
    except OSError:
        print(str(k))
        print('Error')
