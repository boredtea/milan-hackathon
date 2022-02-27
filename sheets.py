# importing the required libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('milan-gargi-44af8bc89f09.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Postal Room')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

# get all the records of the data
records_data = sheet_instance.get_all_records()

# convert the json to dataframe
records_df = pd.DataFrame.from_dict(records_data)

# view the top records
records_df.head()

