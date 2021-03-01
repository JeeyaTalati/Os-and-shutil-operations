import os,shutil
initialFile=input("Enter The File You Need to Back Up")
finalFile=input("Enter The Final Destination Of your Files")
ListOfFiles=os.listdir(initialFile)
for files in ListOfFiles:
    shutil.move((initialFile+"/"+files),(finalFile+"/"))