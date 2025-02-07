from pathlib import Path
import os

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


# creation of file...

def createFile():
    fileName= input("Name your file...")
    filePath=Path(fileName)
    if not filePath.exists():
        with open(filePath, "w") as file:
            data = input("Enter the data you want to write in the file...")
            file.write(data)

        print("File created successfully..!!!!")  

    else:
        print("File already exists...")      


# reading of file...

def readFile():
    fileName= input("Name your file...")
    filePath=Path(fileName)
    if filePath.exists() and filePath.is_file():
        with open(filePath, "r") as file:
            data = file.read()
            print(data)
    else:
        print("File does not exists...")



# updation of file...

def updateFile():
    readFile()
    name = input("File name bolo jisko update krna hai ")
    files = Path(name)
    if files.exists() and files.is_file():
        print("Press 1 for Rename the file")
        print("Press 2 for Overwriting the file")
        print("Press 3 for Append the file")
        choice = int(input("Enter your choice:- "))
        if choice == 1:
            new_name = input("Enter the new name:- ")
            new_file = Path(new_name)
            if not new_file.exists():
                files.rename(new_file)
                print("Rename ho gya ")
            else:
                print("File name already exists ")
        if choice == 2:
            with open(files, "w") as file:
                data = input("Enter the data:- ")
                file.write(data)
            print("Overwrite ho gya ")
        if choice ==3:
            with open(files,"a") as file:
                data = input(" "+"Kya data likhna hai ")   
                file.write(data)
            print("Append ho gya ")



# deletion of file...

def deleteFile():
    fileName= input("Name your file...")
    filePath=Path(fileName)
    if filePath.exists() and filePath.is_file():
        os.remove(filePath)
        print("File deleted successfully..!!!!")

    else:
        print("File does not exists...")        




# main code...

def main():
    print("press 1 for creating a folder: ")
    print("press 2 for reading a folder: ")
    print("press 3 for updating a folder: ")
    print("press 4 for deleting a folder: ")
    print("press 5 for creating a file: ")
    print("press 6 for reading a file: ")
    print("press 7 for updating a file: ")
    print("press 8 for deleting a file: ")

    check = input("give your response...")

    if check =="1":
        createFolder()

    elif check =="2":
        readFolder()

    elif check =="3":
        updateFolder()

    elif check =="4":
        deleteFolder()

    elif check =="5":
        createFile()

    elif check =="6":
        readFile()

    elif check =="7":
        updateFile()    

    elif check =="8":
        deleteFile()    

    else:
        print("please enter the right value !!!")
       
main()