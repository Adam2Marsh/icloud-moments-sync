import iCloudPhotos
import MomentPhotos
import json
import argparse

from hurry.filesize import size

outFolder = ".out/"
resultsFileName = "possible-deletes"

excludeVideoFileExtensions = ['.MOV', '.mp4', '.MP4', '.AVI', '.mov', '.m4v']

def findPhotosWhichCouldBeRemoved(moments, icloud):
    picturesToDelete = []
    spaceSaved = 0
    for momentPhoto in moments:
        if momentPhoto.returnNameWithDate() not in icloud:
            picturesToDelete.append(momentPhoto.returnPath())
            spaceSaved+=momentPhoto.returnFileSizeInBytes()
    
    with open(outFolder + resultsFileName + ".json", 'w', encoding='utf-8') as f:
        json.dump(picturesToDelete, f, ensure_ascii=False, indent=4)
    print('I think there is ' + str(len(picturesToDelete)) + ' to delete which could save ' + size(spaceSaved))

def skipMovieFiles(fileExtensions, name):
    for ext in fileExtensions:
        if ext in name:
            return True
    
    return False


parser = argparse.ArgumentParser(description='Compares your icloud photos with a local copy like moments')
parser.add_argument('icloud_email', type=str, help='Email address used when logging into iCloud')
parser.add_argument('icloud_password', type=str, help='Password used when logging into iCloud')
parser.add_argument('local_directory', type=str, help='Directory which contains local copy of pictures')
parser.add_argument('-ri', '--refresh_icloud', help='Force a refresh of icloud photos', action="store_true")
parser.add_argument('-rl', '--refresh_local', help='Force a refresh of local photos', action="store_true")

args = parser.parse_args()

print(args.icloud_email)

listOfiCloudPhotos = iCloudPhotos.ListOfiCloudPhotos(
        outFolder + 'iCloudLocal.json', args.icloud_email, args.icloud_password, args.refresh_icloud
    )
listOfiCloudPhotos.fetchFileNames()
print("Fetched " + str(len(listOfiCloudPhotos.photos)) + " icloud photos")

listOfMomentPhotos = MomentPhotos.ListOfMomentPhotos(
        outFolder + 'MomentLocal.json', args.local_directory, args.refresh_local
    )

listOfMomentPhotos.fetchFileNames()
print("Fetched " + str(len(listOfMomentPhotos.photos)) + " moment photos")

print("Performing dry-run sync of photos")
findPhotosWhichCouldBeRemoved(listOfMomentPhotos.photos, listOfiCloudPhotos.photos)

print("Saved list of all files which could be deleted in " + outFolder + resultsFileName + '.json')