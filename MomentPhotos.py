from pathlib import Path
import sys
import json

from Utilities import Utilities

class ListOfMomentPhotos:

    def __init__(self, filename):
        self.fileLocation = filename
        self.photos = []
        self.utilities = Utilities()

    def __getFilenames(self):
        momentsFilePath = sys.argv[3]
        momentsFileNames = []

        for path in Path(momentsFilePath).iterdir():
            if path.is_dir():
                for file in Path(path).iterdir():
                    momentsFileNames.append({
                        "name": file.name,
                        "path": str(file)
                    })
        
        with open(self.fileLocation, 'w', encoding='utf-8') as f:
            json.dump(momentsFileNames, f, ensure_ascii=False, indent=4)

    def __loadFilesIntoList(self):
        with open(self.fileLocation) as json_file:            
            for photo in json.load(json_file):
                self.photos.append(
                    MomentPhoto(photo["path"], photo["name"])
                )

    def fetchFileNames(self):
        if self.utilities.checkForFile(self.fileLocation):
            print("Fetching list of filenames and saving locally")
            self.__getFilenames()
        
        print("Loading Photos into Class Array")
        self.__loadFilesIntoList()


class MomentPhoto:
    
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def returnName(self):
        return self.name
    
    def returnPath(self):
        return self.path

    def returnFileSizeInBytes(self):
        return Path(self.path).stat().st_size