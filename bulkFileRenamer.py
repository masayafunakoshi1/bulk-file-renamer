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
    
    i = 0
    # for filename in os.listdir(path):
    #     # if same name but capitalized, it will delete some items, be aware
    #     newName = f'{newName}_' + str(i) + ".jpg"
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



if __name__ == '__main__':
    main()

    