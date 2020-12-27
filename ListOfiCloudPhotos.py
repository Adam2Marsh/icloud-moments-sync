from pyicloud import PyiCloudService
import os
import click
import datetime
import json
import sys

class ListOfiCloudPhotos:

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.iCloudPhotos = []

        if self.checkForFile(self.fileLocation):
            print("iCloud File list doesn't exist so getting")
            self.__logIntoiCloud()
            print("Downloading Filenames from iCloud")
            self.getPhotoNames()
        
        print("Loading Photos into Class Array")
        self.__loadFilesIntoList()
        print(self.iCloudPhotos)
        

    def __logIntoiCloud(self):
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

    def getPhotoNames(self):
        listOfPhotos = []

        for photo in iCloudApi.photos.all:
            print ("Adding " + photo.filename + " to list")
            listOfPhotos.append(photo.filename)

        with open(self.fileLocation, 'w', encoding='utf-8') as f:
            json.dump(listOfPhotos, f, ensure_ascii=False, indent=4)

    def checkForFile(self, filename):
        try:
            with open(filename) as f:
                return False
        except IOError:
            return True
    
    def __loadFilesIntoList(self):
        with open(self.fileLocation) as json_file:            
            for photo in json.load(json_file):
                self.iCloudPhotos.append(iCloudPhoto(photo))
        

class iCloudPhoto:
    
    def __init__(self, name):
        self.name = name

    def returnName(self):
        return self.name