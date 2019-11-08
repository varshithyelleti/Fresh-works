"""

FLAG :
------
1. Flag           : Validates the Input Base Name and Path given by the user.
2. PathFlag       : Validates the  Path given by the user.
3. InputBaseFlag  : Validates the Input Base Name given by the user.

VARIABLES :
-----------
1. Path            : Path of the folder containing the Json files.
2. InputBaseName   : Prefix of the Inpute Json files given by user.
3. OutputBaseName  : Prefix of the Output Json file given by user.
4. MaxFileSize     : Maximum size of the Output file.
5. Counter         : Total Files count in the folder.
6. JsonOutput      : Dictionary which stores the data of the Merged file.
7. InputFiles      : List of the Files in the Jsons folder.
8. ErrorJsonFiles  : List of the Files which have Error in them.
9. OutputFile      : Name of the Output File.
10. exceptions     : List of Exceptions. 

FUNCTIONS :
-----------
1. PathValidator :
   Input  : Path of the Folder containing Json files - string type.
   Output : Boolean value for the existence of folder - True/False.
   
2. InputNameValidator :
   Input  : Input Base Name - string type.
   Output : validates whether the Input Base name and prefix of the
            json files are equal and return boolean value - True/False.
   
3. GetSize :
   Input  : Path of the Folder containing Json files - string type.
   Output : Number of Files in Folder - Int type.
   
4. Main :
   Input  : Driver Function.
   Output : return 0 - Int type.
   
"""

import os
import os.path
import json
from os import path

PathFlag=0
InputBaseFlag=0
PathInputFile=""
Flag=0
Counter=None
JsonOutput={}
InputFiles=[]
ErrorJsonFiles=[]
OutputFile=""
exceptions = IOError,TypeError, RuntimeError, ValueError,PermissionError, FileNotFoundError

def PathValidator(Path):
    return os.path.exists(Path)
    
def InputNameValidator(InputBaseName):
    if(InputBaseName==PathInputFile):
        return True
    else:
        return False
    
def GetSize(Path):
    global PathInputFile,InputFiles
    for dirpath, dirnames, filenames in os.walk(Path):
        Size=len(filenames)-1
        InputFiles=filenames
    InputFiles=InputFiles[:-1]
    Base=filenames[0].split(".")
    Base=Base[0]
    Base=Base[:len(Base)-1]
    PathInputFile=PathInputFile+Base
    return Size

    
def Main():
    global PathFlag,InputBaseFlag,PathInputFile,Flag,Counter
    global JsonOutput,InputFiles,ErrorJsonFiles,OutputFile,exceptions
    Path="C:/Users/varshith yelleti/Desktop/Hit/Assignment-1/"
    InputBaseName="data"
    OutputBaseName="merge"
    MaxFileSize=1000

    Path=input("Enter the Complete Path : ")
    InputBaseName=input("Enter the InputBaseName : ")
    OutputBaseName=input("Enter the OutputBaseName : ")
    MaxFileSize=input("Enter the Max File Size : ")

    while(Flag!=1):
        if(PathFlag==1 or PathValidator(Path)):
            if(PathFlag!=1):
                Counter=GetSize(Path)
            PathFlag=1
            if(InputBaseFlag==1 or InputNameValidator(InputBaseName)):
                InputBaseFlag=1
                Flag=1
                break
            else:
                InputBaseName=input("Enter a vaild Input Base Name : ")
        else:
            Path=input("Enter a vaild Path name : ")
    TotalFileSize=0
    for InputSuffix in InputFiles:
        TFile=Path+InputSuffix
        TotalFileSize+= os.path.getsize(TFile)
        with open(TFile) as InputFilename:
            if len(InputFilename.readlines()) != 0:
                InputFilename.seek(0)
                try:
                    Data = json.load(InputFilename)
                    for key in Data:
                        if(key in JsonOutput):
                            JsonOutput[key]+=Data[key]
                        else:
                            JsonOutput[key]=[]
                            JsonOutput[key]+=Data[key]
                except exceptions as p:
                    Main="File : "+str(InputSuffix)+" has "+ "Error\n"
                    Temp="Correction : "+str(p)+"\n"
                    print(Main)
                    print(Temp)
                    return
            else:
                print("The File : "+str(InputSuffix)+" is empty" )
           
    print("Successfully Merged ")
    OutputFile+=OutputBaseName+"1.json"
    with open(OutputFile, 'w') as json_file:
        json.dump(JsonOutput, json_file)
    FileSize= os.path.getsize(OutputFile)
    print("Merged File Size : ",FileSize)
    return 0

if __name__ == '__main__':
    Main()




