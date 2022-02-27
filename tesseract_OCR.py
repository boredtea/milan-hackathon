import cv2
import pytesseract
import pandas as pd
import os

# path to tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\soumi\AppData\Local\Programs\Tesseract-OCR\tesseract'

# imageText = pytesseract.image_to_string(r'C:\Users\soumi\Documents\Code_stuff\Various_Projects\milan-hackathon\amazonPacket2.jpeg')
csv_path = 'parcels.csv'
imagePath = r'C:\Users\soumi\Documents\Code_stuff\Various_Projects\milan-hackathon\amazonPacket2.jpeg'

# scan image
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            # cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            break
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



imageText = pytesseract.image_to_string(gray)


lines = imageText.split('\n')
lines = list(filter(None, lines))
print(type(imageText))
print(imageText)
print(lines)
index_awb = 0
index_name = 0
for word in lines:
    if word.find("AWB") != 1:
        index_awb = lines.index(word) + 1
        index_name = index_awb + 1
        break

print("AWB: ", lines[index_awb])
print("Name: ", lines[index_name])

if os.path.isfile(csv_path):
    df = pd.read_csv(csv_path)
    print(df)
    # new_row = {"AWB": lines[index_awb], "Name": lines[index_name]}
    # df = df.append(new_row)

    # new_row = pd.Series({"AWB": [lines[index_awb]], "Name": [lines[index_name]]})
    # df = pd.concat([df, new_row], axis = 0)
    df.loc[df.shape[0]] = [lines[index_awb], lines[index_name]]

else:
    data = {"AWB": [str(lines[index_awb])], "Name": [str(lines[index_name])]}
    df = pd.DataFrame(data)

df.to_csv(csv_path)

