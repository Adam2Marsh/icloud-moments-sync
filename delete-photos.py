import json
import argparse
import os
import shutil

from Utilities import Utilities
from MomentPhotos import MomentPhoto

outFolder = ".out/"
resultsFileName = "possible-deletes"

utils = Utilities()

parser = argparse.ArgumentParser(description='Removes files from moments but moving files found in find-photos-to-delete.py')
parser.add_argument('recycle_bin', type=str, help='Path to directory to move files to')
args = parser.parse_args()

if utils.checkForFile(outFolder + resultsFileName + ".json"):
    if os.path.isdir(args.recycle_bin):
        
        with open(outFolder + resultsFileName + ".json") as json_file:            
            for photo in json.load(json_file):
                momentPhoto = MomentPhoto(photo)
                shutil.move(momentPhoto.returnPath(), args.recycle_bin + "/" + momentPhoto.returnFileName())
    
        print("All photos have been moved to " + args.recycle_bin + ", if happy you can delete")

    else:
        print("Please check your recycle_bin directory exists")
else:
    print("Unable to find " + resultsFileName + ".json, please run find-photos-to-delete.py first")