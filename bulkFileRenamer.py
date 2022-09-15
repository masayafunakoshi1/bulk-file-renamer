import os

def main():
    print("Welcome to the bulk-file-renamer! Using this script lets you rename all the files in a folder of your choosing!")
    print("It changes the name and indexes it starting from 0")
    print("e.g. Rename IMG3124.jpg --> Picture --> picture_0.jpg")
    i = 0
    # for paths, make sure to use mnt/d
    print("Input path to folder: ")
    path = validPathCheck()
    print("Input edited name (spaces will be _): ")
    editedName = input()
    for filename in os.listdir(path):
        # if same name but capitalized, it will delete some items, be aware
        editedName = "City_snaps_" + str(i) + ".jpg"
        my_source =path + filename
        editedName =path +  editedName
        os.rename(my_source,  editedName)
        i += 1

def validPathCheck():
    temp = input()
    if(os.path.exists(temp) != True):
        print("Path not found.")
        return
    else:
        return temp

if __name__ == '__main__':
    main()

    