import ListOfiCloudPhotos

outFolder = ".out/"
momentsFileName = "momentsPhotoFileNames"
resultsFileName = "results"

excludeVideoFileExtensions = ['.MOV', '.mp4', '.MP4', '.AVI', '.mov', '.m4v']

localConfigDict = {}


# def getFilenamesFromMoments():
#     momentsFilePath = sys.argv[3]
#     momentsFileNames = []

#     for path in Path(momentsFilePath).iterdir():
#         if path.is_dir():
#             for file in Path(path).iterdir():
#                 print ("Adding " + file.parts[-1] + " to list with path of " + str(file))
#                 momentsFileNames.append({
#                     "name": file.name,
#                     "path": str(file)
#                 })
    
#     with open(outFolder + momentsFileName + ".json", 'w', encoding='utf-8') as f:
#         json.dump(momentsFileNames, f, ensure_ascii=False, indent=4)

# def loadFileIntoConfigDict(fileName):
#     with open(outFolder + fileName + '.json') as json_file:
#         fileContents = json.load(json_file)
#         localConfigDict[fileName] = fileContents

# def findPhotosWhichCouldBeRemoved(moments, icloud):
#     picturesToDelete = []
#     spaceSaved = 0
#     for photo in localConfigDict[moments]:
#         photoObject = MomentPhoto(photo["path"], photo["name"])
#         if not skipMovieFiles(excludeVideoFileExtensions, photoObject.name):
#             if photoObject.name not in localConfigDict[two]:
#                 print (photoObject.name + ' not exists ' + two + '; so could be one to delete')
#                 picturesToDelete.append(photoObject.name)
    
#     with open(outFolder + "delete.json", 'w', encoding='utf-8') as f:
#         json.dump(picturesToDelete, f, ensure_ascii=False, indent=4)
#     print('I think there is ' + str(len(picturesToDelete)) + ' to delete')

# def skipMovieFiles(fileExtensions, name):
#     for ext in fileExtensions:
#         if ext in name:
#             return True
    
#     return False

listOfiCloudPhotos = ListOfiCloudPhotos.ListOfiCloudPhotos(outFolder + 'iCloudLocal.json')

# print("Starting sync process")
# if checkForFile(outFolder + iCloudFileName):

# else:
#     print("iCloud Filenames Already Fetched")

# if checkForFile(outFolder + momentsFileName):
#     print("Moments File list doesn't exist so getting")
#     getFilenamesFromMoments()
# else:
#     print("Moments Filenames Already Fetched")

# loadFileIntoConfigDict(iCloudFileName)
# loadFileIntoConfigDict(momentsFileName)

# findPhotosWhichCouldBeRemoved(iCloudFileName, momentsFileName)