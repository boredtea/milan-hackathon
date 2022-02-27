# milan-hackathon# milan-hackathon

# Index
---------------------
   
 * Introduction
 * Requirements
 * Compiling
 * Usage
 * Features
 * Future Scope

## INTRODUCTION
------------

The process of manually writing details of parcels in the postal office is a long and tedious process. Our project aims to automate this process. Once you scan a parcel (can be done using a phone camera), its details are stored in a database and students can lookup the status of their parcels using order id, name, etc.

## REQUIREMENTS
------------

The programs require the following softwares/files/tools:

 * python
 * pytesseract
 * [tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
 * [Droid Cam](https://www.dev47apps.com/droidcam/windows/)
 * A webcam or another video stream source 
 * pip intall gspread
 * pip install --upgrade google-api-python-client oauth2client

## EXECUTION
------------
 
 * In the file named `tesseract_OCR.py`, change `pytesseract.pytesseract.tesseract_cmd` to the path where tesseract was installed.
 * Also update `csv_path` to the path where the local csv is located.
 * Update the `cv2.VideoCapture(1)` index to the appropriate camera.
 * Execute the command `python tesseract_OCR.py` from the terminal.
 * Execute the command `python tesseract_OCR_sheet.py` from the terminal to make changes to Google sheet which is public.

## USAGE
-----
 
 * Once the camera preview shows up, scan the label text with your carema device. Press `s` when you've positioned the camera over the label as required. The index, AWB and the name from the label is entered into the csv file.
 * Repeat the above step to scan the next label.
 * To stop scanning, press `q`.

 ## FEATURES
------------
* The local csv file gets uploaded to a public google sheet where students can easily search via their name/AWB. Once they've collected their parcel the postal room can edit the sheet as required.
* The indexing in the sheet also hels the postal room since that is doesn't change their current organising techniques.
* Google Sheets serve as frontend to the public on a large scale. The public sheet can be found here: [Postal Room](https://docs.google.com/spreadsheets/d/1irjbTqD7PK7vBUHshxY_KLiqYmCUezauY8wChp9GyAo/edit?usp=sharing)

 ## FUTURE SCOPE
------------
* We want to make it work for all kinds of parcels.
* An app for users to search for their parcels.
* Making the search feature more secure by adding login and other security features. 
* A notification system for the students once a parcel is received.
* A website for the postal office side to store and view records.