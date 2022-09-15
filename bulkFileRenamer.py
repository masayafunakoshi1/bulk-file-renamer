import os
import re

def main():
    print("Welcome to the bulk-file-renamer! Using this script lets you rename all the files in a folder of your choosing!")
    print("It changes the name and indexes it starting from 0")
    print("e.g. Rename IMG3124.jpg --> Picture --> picture_0.jpg")
    print("-----------------------------------------")

    # for paths, make sure to use mnt/d
    path = input("Input path to folder: ")
    if(validPathCheck(path) != True): 
        return

    print("-----------------------------------------")
    print("Input edited name (NO SPACES or SPECIAL CHARACTERS besides - or _): ")
    newName = validFileName()

    i = 0
    # for filename in os.listdir(path):
    #     # if same name but capitalized, it will delete some items, be aware
    #     newName = f'{newName}_' + str(i) + ".jpg"
    #     my_source =path + filename
    #     newName =path +  newName
    #     os.rename(my_source,  newName)
    #     i += 1

#checks if file path is valid
def validPathCheck(path):
    if os.path.exists(path) != True:
        print("Path set failed. Path not found.")
        return False
    else:
        print("Path set successfully.")
        return True

#Checks if inputted filename is valid and sets it
def validFileName():
    attemptedName = input()
    regex = re.compile("[@!#$%^&*()<>?/\|}{~;:,.`\'\"\[\]\s]") 
    while(True):
        if(regex.search(attemptedName) == None):
            print("File name set successfully!")
            return attemptedName
        else:
            print("Invalid file Name. Reinput new valid file name:")
            attemptedName = input()


if __name__ == '__main__':
    main()

    