import cv2
import datetime
import re
import struct
import os
import csv
import random
import pyautogui as pa
import pytesseract
import pyscreenshot as ps
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt

def wiredFileTransfer(filenames, device_path):
    for filename in filenames:
        os.rename(filename, os.path.join(device_path, os.path.basename(filename)))
    print('Done')


def ServerFileUpload(filenames):
    prev_files = os.listdir('static/exam_cheater')
    for file in prev_files:
        os.remove(os.path.join('static/exam_cheater', file))
    for filename in filenames:
        os.rename(filename, os.path.join('static/exam_cheater',os.path.basename(filename)))

def create_quick_subplots(filenames):
    row=1
    col =len(filenames)
    for i in range(len(1, filenames)):
        if (len(filenames)%i) == 0:
            if len(filenames)/i < col:
                row = i
                col = len(filenames)/i
    fig, axs = plt.subplots(row,col,figsize=(5,5))
    index = 0
    for r in range(row):
        for c in range(col):
            im = cv2.imread(filenames[index])
            axs[r][c].imshow(im)
            index += 1
    plt.show()

    
def webSearchExam(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

    searches = list(search(query, tld = "com", num = 10, stop =10, pause =2))
    # print(searches)
    pattern = re.compile(r'(http|https)?(://)(www\.)?(stackoverflow|quora|geeksforgeeks|answers|stackexchange)(\.\w{2,4})(.*)')
    matches = list(filter(pattern.match, searches))
    filenames=[]
    # print(matches)
    for index in range(len(matches)):
        match = matches[index]
        print(match)
        driver.get(match)
        website_name = re.compile(r'(http|https)?(://)(www\.)?(\w+)(\.\w{2,4})/([\w*|\d*-]+)/?').findall(match)
        file_name= 'temp/{}-{}_{}.png'.format(website_name[0][3], website_name[0][5], str(index))
        filenames.append(file_name)
        print('filename: {}'.format(file_name))
        driver.get_screenshot_as_file(file_name)
    return filenames


def webSearchPersonal(query):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')
    searches = list(search(query, tld = "com", num = 10, stop =10, pause =2))
    # print(searches)
    pattern = re.compile(r'(http|https)?(://)(www\.)?(medium|towardsdatascience|wikipedia|youtube|stackoverflow|quora|geeksforgeeks|answers|stackexchange)(\.\w{2,4})(.*)')
    matches = list(filter(pattern.match, searches))
    driver.get(matches[0])
    for index in range(1,len(matches)):
        match = matches[index]
        driver.execute_script('''window.open("{}","_blank");'''.format(match))

def OCR(orig_filename):
    im = cv2.imread(orig_filename)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    text = ' '.join(pytesseract.image_to_string(gray).split('\n'))
    os.remove(filename)
    return text

def execute_cliper():
    x1,y1= pa.position()
    code = 1
    event = in_file.read(EVENT_SIZE)
    while code != 45:
        (_,_,type, code, value) = struct.unpack(FORMAT, event)
        event = in_file.read(EVENT_SIZE)
    x2,y2 = pa.position()
    im = ps.grab(bbox=(min(x1,x2),min(y1,y2),max(x1,x2),max(y1,y2)))
    # if x1<x2:
    #     im = ps.grab(bbox=(x1,y1,x2,y2))
    # elif x2<x1:
    #     im = ps.grab(bbox=(x2,y2,x1,y1))
    print('capture complete')
    filename=os.path.join('capture',str(datetime.datetime.now())+'.png')
    im.save(filename)
    return im, filename



Mobile_storage_path='/run/user/1000/gvfs/mtp:host=%5Busb%3A001%2C006%5D/Samsung SD card/cheeter/'

qwerty_map = {
    2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9",
    11: "0", 12: "-", 13: "=", 14: "[BACKSPACE]", 15: "[TAB]", 16: "a", 17: "z",
    18: "e", 19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p", 26: "^",
    27: "$", 28: "\n", 29: "[CTRL]", 30: "q", 31: "s", 32: "d", 33: "f", 34: "g",
    35: "h", 36: "j", 37: "k", 38: "l", 39: "m", 40: "ù", 41: "*", 42: "[SHIFT]",
    43: "<", 44: "w", 45: "x", 46: "c", 47: "v", 48: "b", 49: "n", 50: ",",
    51: ";", 52: ":", 53: "!", 54: "[SHIFT]", 55: "FN", 56: "ALT", 57: " ", 58: "[CAPSLOCK]",
}


FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

file_name = '/dev/input/event4'
in_file = open(file_name, 'rb')
event = in_file.read(EVENT_SIZE)
exam_activator = 'hooded'
personal_use_activator = 'hare'
typed = ""
check =0
while event:
    try:
        (_,_,type, code, value) = struct.unpack(FORMAT, event)
        if code != 0 and type ==1 and value ==1:
            if code in qwerty_map:
                    typed += qwerty_map[code]
        event = in_file.read(EVENT_SIZE)
        if code == 14:
            print('restarted.... reset code excepted')
            typed = ""
            check = 0
        elif typed == exam_activator:
            print('exam_activator idetified----- Starting the hidden action...... ')
            check += 1
            print(check)
            if check == 6:
                snipped_im, filename = execute_cliper()
                text = OCR(filename)
                print(text)
                csv_file=open('ocr_info.csv','a+')
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([filename, text])
                csv_file.close()
                filenames = webSearchExam(text)
                # wiredFileTransfer(filenames, Mobile_storage_path)
                # wirelessFileTransfer(filenames)
                ServerFileUpload(filenames)

        elif typed == personal_use_activator:
            print('personal_use_activator idetified----- Starting the hidden action...... ')
            check += 1
            print(check)
            if check == 6:
                snipped_im, filename = execute_cliper()
                text = OCR(filename)
                print(text)
                csv_file=open('ocr_info.csv','a+')
                csv_writer=csv.writer(csv_file)
                csv_writer.writerow([filename, text])
                csv_file.close()
                webSearchPersonal(text)

        elif len(typed) > max(len(exam_activator), len(personal_use_activator)):
            # print('restarted.... Wrong activator identified')
            typed = ""
            check =0
    except Exception as e:
        print(e)
        import os
        beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
        beep(3)
