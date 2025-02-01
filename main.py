from pathlib import Path

# folder creation function...

def createFolder():
    folderName= input("Name your folder...")
    folderPath=Path(folderName)
    folderPath.mkdir()
    print(" Folder created successfully..!!!!")


# reading folder function...

def readFolder():
    path= Path("")
    items = list(path.rglob("*"))
    for i,v in enumerate(items):
        print(f"{i+1}. {v}")



#updation of folder...

def updateFolder():
    readFolder()
    oldName= input("Enter the name of the folder you want to update...")
    oldPath=Path(oldName)
    if oldPath.exists() and oldPath.is_dir():
        newFolderName= input("Enter the new name of the folder...")
        newPath=Path(newFolderName)
        if not newPath.exists():
            oldPath.rename(newPath)
            print("Name updated successfully...!!!")
        else:
            print("Folder already exists...")
    

# deletion of  folder...

def deleteFolder():
    readFolder()
    folderName= input("Name your folder...")
    folderPath=Path(folderName)
    if folderPath.exists() and folderPath.is_dir():
        folderPath.rmdir()
        print(" Folder deleted successfully..!!!!")

    else:
        print("no folder present..")    



# main code...

print("press 1 for creating a folder: ")
print("press 2 for reading a folder: ")
print("press 3 for updating a folder: ")
print("press 4 for deleting a folder: ")


check = input("give your response...")

if check =="1":
    createFolder()

elif check =="2":
    readFolder()

elif check =="3":
    updateFolder()

elif check =="4":
    deleteFolder()

else:
    print("please enter the right value !!!")    

        