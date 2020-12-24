import os
import click
import datetime
import json
import sys
from pyicloud import PyiCloudService
from pathlib import Path

outFolder = ".out/"
iCloudFileName = "iCloudPhotoFileNames"
momentsFileName = "momentsPhotoFileNames"
resultsFileName = "results"

excludeVideoFileExtensions = ['.MOV', '.mp4', '.MP4', '.AVI', '.mov', '.m4v']

localConfigDict = {}

def logIntoiCloud():
    global iCloudApi

    print("Logging into iCloud")
    iCloudApi = PyiCloudService(sys.argv[1], sys.argv[2])

    if iCloudApi.requires_2sa:
        print("Two-factor authentication required. Your trusted devices are:")

        devices = iCloudApi.trusted_devices
        for i, device in enumerate(devices):
            print(
                "  %s: %s"
                % (i, device.get("deviceName", "SMS to %s" % device.get("phoneNumber")))
            )

        device = click.prompt("Which device would you like to use?", default=0)
        device = devices[device]
        if not iCloudApi.send_verification_code(device):
            print("Failed to send verification code")
            sys.exit(1)

        code = click.prompt("Please enter validation code")
        if not iCloudApi.validate_verification_code(device, code):
            print("Failed to verify verification code")
            sys.exit(1)

def getFilenamesFromiCloud():
    listOfPhotos = []

    for photo in iCloudApi.photos.all:
        print ("Adding " + photo.filename + " to list")
        listOfPhotos.append(photo.filename)

    with open(outFolder + iCloudFileName + ".json", 'w', encoding='utf-8') as f:
        json.dump(listOfPhotos, f, ensure_ascii=False, indent=4)

def checkForFile(filename):
    try:
        with open(filename + ".json") as f:
            return False
    except IOError:
        return True

def getFilenamesFromMoments():
    momentsFilePath = sys.argv[3]
    momentsFileNames = []

    for path in Path(momentsFilePath).iterdir():
        if path.is_dir():
            for file in Path(path).iterdir():
                print ("Adding " + file.parts[-1] + " to list")
                momentsFileNames.append(file.parts[-1])
    
    with open(outFolder + momentsFileName + ".json", 'w', encoding='utf-8') as f:
        json.dump(momentsFileNames, f, ensure_ascii=False, indent=4)

def loadFileIntoConfigDict(fileName):
    with open(outFolder + fileName + '.json') as json_file:
        fileContents = json.load(json_file)
        localConfigDict[fileName] = fileContents

def compareFiles(one, two):
    picturesToDelete = []
    for photoName in localConfigDict[one]:
        if not skipMovieFiles(excludeVideoFileExtensions, photoName):
            if photoName not in localConfigDict[two]:
                print (photoName + ' not exists ' + two + '; so could be one to delete')
                picturesToDelete.append(photoName)
    
    with open(outFolder + "delete.json", 'w', encoding='utf-8') as f:
        json.dump(picturesToDelete, f, ensure_ascii=False, indent=4)
    print('I think there is ' + str(len(picturesToDelete)) + ' to delete')

def skipMovieFiles(fileExtensions, name):
    for ext in fileExtensions:
        if ext in name:
            return True
    
    return False

print("Starting sync process")
if checkForFile(outFolder + iCloudFileName):
    print("iCloud File list doesn't exist so getting")
    logIntoiCloud()

    print("Downloading Filenames from iCloud")
    getFilenamesFromiCloud()
else:
    print("iCloud Filenames Already Fetched")

if checkForFile(outFolder + momentsFileName):
    print("Moments File list doesn't exist so getting")
    getFilenamesFromMoments()
else:
    print("Moments Filenames Already Fetched")

loadFileIntoConfigDict(iCloudFileName)
loadFileIntoConfigDict(momentsFileName)

compareFiles(iCloudFileName, momentsFileName)