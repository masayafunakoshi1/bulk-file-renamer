import os
import re

def main():
    print("Welcome to the bulk-file-renamer! Using this script lets you rename all the files in a folder of your choosing!")
    print("It changes the name and indexes it starting from 0")
    print("e.g. Rename IMG3124.jpg --> Picture --> picture_0.jpg")
    print("-----------------------------------------")
    # for paths, make sure to use mnt/d
    path = validPathCheck()

    print("-----------------------------------------")
    newName = validFileName()

    print("-----------------------------------------")
    fileType = chooseFileType()

    i = 0
    # for filename in os.listdir(path):
    #     # if same name but capitalized, it will delete some items, be aware
    #     newName = f'{newName}_' + str(i) + fileType
    #     my_source =path + filename
    #     newName =path +  newName
    #     os.rename(my_source,  newName)
    #     i += 1

#checks if file path is valid
def validPathCheck():
    path = input("Input path to folder: ")
    while(True):
        if os.path.exists(path) != True:
            print("Path set failed. Path not found.")
            path = input("Try different path: ")
        else:
            print("Path set successfully!")
            return path

#Checks if inputted filename is valid and sets it
def validFileName():
    attemptedName = input("Input edited name (NO SPACES or SPECIAL CHARACTERS besides - or _): ")
    regex = re.compile("[@!#$%^&*()<>?/\|}{~;:,.`\'\"\[\]\s]") 
    while(True):
        if(regex.search(attemptedName) != None):
            print("Invalid filename.")
            attemptedName = input("Try different filename: ")
        else:
            print("Filename set successfully!")
            return attemptedName

def chooseFileType():
    # for now just img types
    # add from here later: https://www.computerhope.com/issues/ch001789.htm 
    while(True):
        fileType = input("Pick file type: \n 1) jpg   2) png   3) gif \n 4) svg   5) tif   6) psd \n 7) ico   8) bmp   9) ai \n 10) ps \n\nType number here:")
        if fileType == "1":
            print(".jpg picked.")
            return ".jpg" 
        elif fileType == "2":
            print(".png picked.")
            return ".png"
        elif fileType == "3":
            print(".gif picked.")
            return ".gif" 
        elif fileType == "4":
            print(".svg picked.")
            return ".svg" 
        elif fileType == "5":
            print(".tif picked.")
            return ".tif" 
        elif fileType == "6":
            print(".psd picked.")
            return ".psd" 
        elif fileType == "7":
            print(".ico picked.")
            return ".ico" 
        elif fileType == "8":
            print(".bmp picked.")
            return ".bmp" 
        elif fileType == "9":
            print(".ai picked.")
            return ".ai" 
        elif fileType == "10":
            print(".ps picked.")
            return ".ps"
        else:  
            print("Invalid file type.")
            print("-----------------------------------------")
            fileType = input("Pick file type: \n 1) jpg   2) png   3) gif \n 4) svg   5) tif   6) psd \n 7) ico   8) bmp   9) ai \n 10) ps \n\nType number here:")

if __name__ == '__main__':
    main()

    