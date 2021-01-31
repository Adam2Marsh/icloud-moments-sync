from pathlib import Path
import sys
import json

from Utilities import Utilities

class ListOfMomentPhotos:

    def __init__(self, filename, local_directory, refresh):
        self.fileLocation = filename
        self.local_directory = local_directory
        self.refresh = refresh
        self.photos = []
        self.utilities = Utilities()

    def __getFilenames(self):
        momentsFilePath = sys.argv[3]
        momentsFileNames = []

        for path in Path(momentsFilePath).iterdir():
            if path.is_dir():
                for file in Path(path).iterdir():
                    momentsFileNames.append({
                        "path": str(file)
                    })
        
        with open(self.fileLocation, 'w', encoding='utf-8') as f:
            json.dump(momentsFileNames, f, ensure_ascii=False, indent=4)

    def __loadFilesIntoList(self):
        with open(self.fileLocation) as json_file:            
            for photo in json.load(json_file):
                self.photos.append(
                    MomentPhoto(photo["path"])
                )

    def fetchFileNames(self):
        if self.utilities.checkForFile(self.fileLocation) == False or self.refresh:
            print("Fetching list of filenames and saving locally")
            self.__getFilenames()
        
        print("Loading Photos into Class Array")
        self.__loadFilesIntoList()


class MomentPhoto:
    
    def __init__(self, path):
        self.path = path

    def returnNameWithDate(self):
        return self.returnPathDate() + "/" + self.returnName()

    def returnName(self):
        return self.returnFileName().split(".")[0]
    
    def returnFileName(self):
        return self.path.split("/")[-1]

    def returnPath(self):
        return self.path

    def returnPathDate(self):
        return self.path.split("/")[-2]

    def returnFileSizeInBytes(self):
        return Path(self.path).stat().st_size