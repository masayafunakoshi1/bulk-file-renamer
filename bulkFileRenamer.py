import os

def main():
    i = 0
    # for paths, make sure to use mnt/d
    print("Input ")
    path = "/mnt/d/Coding/Python/Learning/renamedFolder/"
    for filename in os.listdir(path):
        # if same name but capitalized, it will delete some items, be aware
        editedName = "City_snaps_" + str(i) + ".jpg"
        my_source =path + filename
        editedName =path +  editedName
        os.rename(my_source,  editedName)
        i += 1


if __name__ == '__main__':
    main()


    