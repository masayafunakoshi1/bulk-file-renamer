import os

def main():
    print("Welcome to the bulk-file-renamer! Using this script lets you rename all the files in a folder of your choosing!")
    print("It changes the name and indexes it starting from 0")
    print("e.g. Rename IMG3124.jpg --> Picture --> picture_0.jpg")

    # for paths, make sure to use mnt/d
    print("Input path to folder: ")
    path = input()
    if(validPathCheck(path) != True): 
        return

    print("Input edited name (spaces will be _): ")
    editedName = input()
    

    i = 0
    for filename in os.listdir(path):
        # if same name but capitalized, it will delete some items, be aware
        editedName = "temp" + str(i) + ".jpg"
        my_source =path + filename
        editedName =path +  editedName
        os.rename(my_source,  editedName)
        i += 1

def validPathCheck(path):
    if(os.path.exists(path) != True):
        print("Path set failed. Path not found.")
        return False
    else:
        print("Path set successfully.")
        return True

if __name__ == '__main__':
    main()

    