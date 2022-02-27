import cv2
import pytesseract
import pandas as pd
import os
import csv 
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\soumi\AppData\Local\Programs\Tesseract-OCR\tesseract'

# csv path
csv_path = r'parcels.csv'

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

# scan image
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(1)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)

        # if s is pressed, make entry in the csv
        if key == ord('s'):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            imageText = pytesseract.image_to_string(gray)

            lines = imageText.split('\n')
            lines = list(filter(None, lines))
            print(lines)
            index_awb = 0
            index_name = 0
            # find index of AWB number and the name
            for word in lines:
                if word.find("AWB") != 1:
                    index_awb = lines.index(word) + 1
                    index_name = index_awb + 1
                    break
            
            # create csv if it doesn't exist, add column names
            if not(os.path.isfile(csv_path)):
                with open(csv_path, 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Index", "AWB", "Name"])

            # update csv
            df = pd.read_csv(csv_path)
            index = df.shape[0]
            data = [index, lines[index_awb], lines[index_name]]
            sheet_instance.insert_rows(data)
            # with open(csv_path, 'a') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(data)

            print("Added")
            # break
        # exit loop if q is pressed
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break