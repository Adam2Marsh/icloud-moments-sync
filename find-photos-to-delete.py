import iCloudPhotos
import MomentPhotos
import json

from hurry.filesize import size

outFolder = ".out/"
resultsFileName = "possible-deletes"

excludeVideoFileExtensions = ['.MOV', '.mp4', '.MP4', '.AVI', '.mov', '.m4v']

def findPhotosWhichCouldBeRemoved(moments, icloud):
    picturesToDelete = []
    spaceSaved = 0
    for photo in moments:
        # if not skipMovieFiles(excludeVideoFileExtensions, photo.returnName()):
        if photo.returnName() not in icloud:
            # print (photo.returnName() + ' does not exist in iCloud; so could be one to delete')
            picturesToDelete.append(photo.returnName())
            spaceSaved+=photo.returnFileSizeInBytes()
    
    with open(outFolder + resultsFileName + ".json", 'w', encoding='utf-8') as f:
        json.dump(picturesToDelete, f, ensure_ascii=False, indent=4)
    print('I think there is ' + str(len(picturesToDelete)) + ' to delete which could save ' + size(spaceSaved))

def skipMovieFiles(fileExtensions, name):
    for ext in fileExtensions:
        if ext in name:
            return True
    
    return False

listOfiCloudPhotos = iCloudPhotos.ListOfiCloudPhotos(outFolder + 'iCloudLocal.json')
listOfiCloudPhotos.fetchFileNames()
print("Fetched " + str(len(listOfiCloudPhotos.photos)) + " icloud photos")

listOfMomentPhotos = MomentPhotos.ListOfMomentPhotos(outFolder + 'MomentLocal.json')
listOfMomentPhotos.fetchFileNames()
print("Fetched " + str(len(listOfMomentPhotos.photos)) + " moment photos")

print("Performing dry-run sync of photos")
findPhotosWhichCouldBeRemoved(listOfMomentPhotos.photos, listOfiCloudPhotos.photos)

print("Saved list of all files which could be deleted in " + outFolder + resultsFileName + '.json')