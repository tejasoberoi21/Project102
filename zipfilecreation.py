import zipfile
import os

files = []
while True:
    inputVal = input("Enter a filename and path to be compressed into a zip file, enter STOP to quit: ")
    if(inputVal == "STOP"):
        break
    files.append(inputVal)

name = input("Enter name of zip file: ")
with zipfile.ZipFile(name + ".zip", 'w') as new_zip:
    for file in files:
        new_zip.write(file)
        
