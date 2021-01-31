from pyicloud import PyiCloudService
import os
import click
import datetime
import json
import sys
import argparse

from Utilities import Utilities

class ListOfiCloudPhotos:

    def __init__(self, fileLocation, icloud_email, icloud_password, refresh):
        self.fileLocation = fileLocation
        self.icloud_email = icloud_email
        self.icloud_password = icloud_password
        self.refresh = refresh
        self.objectPhotos = []
        self.photos = []
        self.utilities = Utilities()

    def __logIntoiCloud(self):
        global iCloudApi

        print("Logging into iCloud")
        iCloudApi = PyiCloudService(self.icloud_email, self.icloud_password)

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

    def __getPhotoNames(self):
        listOfPhotos = []

        for photo in iCloudApi.photos.all:
            # print ("Adding " + photo.filename + " to list")
            listOfPhotos.append({
                "name": photo.filename,
                "added_date": photo.added_date.isoformat(),
                "asset_date": photo.asset_date.isoformat()
            })

        with open(self.fileLocation, 'w', encoding='utf-8') as f:
            json.dump(listOfPhotos, f, ensure_ascii=False, indent=4)
    
    def __loadFilesIntoList(self):
        with open(self.fileLocation) as json_file:            
            for photo in json.load(json_file):
                photoObject = iCloudPhoto(photo["name"], photo["asset_date"])
                self.photos.append(photoObject.returnDate() + "/" + photoObject.returnName())
                # self.photos.append(photoObject)
        
    def fetchFileNames(self):
        if self.utilities.checkForFile(self.fileLocation) == False or self.refresh:
            print("iCloud File list doesn't exist so getting")
            self.__logIntoiCloud()
            print("Downloading Filenames from iCloud")
            self.__getPhotoNames()
        
        print("Loading Photos into Class Array")
        self.__loadFilesIntoList()
        
class iCloudPhoto:
    
    def __init__(self, filename, date):
        self.filename = filename
        self.date = date

    def returnFilename(self):
        return self.filename

    def returnName(self):
        return self.filename.split(".")[0]

    def returnDate(self):
        return self.date.split("T")[0]