# Junk file organizer

import os
import shutil
import os.path
import time

from datetime import datetime

# this function is used to sort files by extension


def byextension():

    path = input("enter path directory :-")
    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

    # List only the files in the folder
    # files = [f for f in os.listdir(
    # path) if os.path.isfile(os.path.join(path, f))]
    # change the current path

    os.chdir(path)

    arr = os.listdir()

    slash = "\\"

    file_types = {
        "Docs": [".doc", ".rtf", ".txt", ".wps", ".docx"],
        "Data": [".csv", ".pps", ".ppt", ".pptx", ".xml"],
        "Music": [".mp3", ".m4a", ".m4a",  ".m4p", ".mp3", "ogg"],
        "Video": [".3gp", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".wmv"],
        "notes": [".pdf"],
        "Spreadsheet": [".xlr", ".xls", ".xlsx"],
        "apps": [".apk", ".app", ".exe", ".jar"],
        "Web": [".css", ".htm", ".html", ".js", ".php", ".xhtml"],
        "Compressed": [".rar", ".zip"],
        "Programmes": [".c", ".class", ".cpp", ".cs", ".java", ".py"],
        "Misc": [".ics", ".msi", ".torrent"],
        "images": [".jpeg", ".png", ".jpg"]
    }

    for x in arr:
        fflag = 0
        if os.path.isfile(x):
            if("." in x):
                extension_name = x[x.index("."):]
                for file_type, extensions in file_types.items():
                    if extension_name in extensions:
                        fflag = 1
                        folder_name = file_type
                        newpath = path + slash + folder_name
                        print(newpath)
                        break
                if (fflag == 0):
                    folder_name = "Other"
                    newpath = path + slash + folder_name
                    print(newpath)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(path + slash + x, newpath + slash + x)


# this function is used to sort by date

def bydate():
    path = input("enter path directory :-")
    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]

    os.chdir(path)
    for x in files:

        modified_time_string = time.ctime(
            os.path.getmtime(os.path.join(path, x)))

        modified_datetime_obj = datetime.strptime(
            modified_time_string, '%a %b %d %H:%M:%S %Y')

        modified_date = str(modified_datetime_obj.day) + '-' + str(
         modified_datetime_obj.month) + '-' + str(modified_datetime_obj.year)

        if(os.path.isdir(modified_date)):
            shutil.move(os.path.join(path, x), modified_date)

        else:

            os.makedirs(modified_date)
            shutil.move(os.path.join(path, x), modified_date)


# this function is used to count the files

def count_files():

    # Path where we have to count files and directories

    path = input("enter the path :-")

    n = 0

    for base, dirs, files in os.walk(path):

        print('Looking in : ', base)

        for Files in files:

            n += 1

    print('Number of files', n)


# this function is used to know the size


def size():

    path = input("enter your directory path:-")

    size = 0

    fsizedicr = {'Bytes': 1, 'Kilobytes': float(
     1)/1024, 'Megabytes': float(
         1)/(1024*1024), 'Gigabytes': float(1)/(1024*1024*1024)}

    for (path, dirs, files) in os.walk(path):

        for file in files:
            filename = os.path.join(path, file)
            size += os.path.getsize(filename)

    for key in fsizedicr:
        print("Folder Size: " + str(round(fsizedicr[key]*size, 2)) + " " + key)


print("""PRESS 1 TO ORGANIZE FILES BY EXTENSION
PRESS 2 TO  ORGANIZE FILES BY DATE
PRESS 3 TO  COUNT FILES IN YOUR DIRECTORY
PRESS 4 TO KNOW THE SIZE OF FILES IN YOUR  DIRECTORY""")

op = int(input("ENTER YOUR OPTION:-"))

if op == 1:
    byextension()

elif op == 2:
    bydate()

elif op == 3:
    count_files()

elif op == 4:
    size()
