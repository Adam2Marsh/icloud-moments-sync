## Overview
I developed these 2 scripts to remove pictures from Synology moments which had been synced via the app but deleted from iCloud. The 2 scripts do the following:
* find-photos-to-delete.py - This one will connect to the iCloud API and grab a list of all your photos, then save that as a json file in the .out directory. It will then read all the photos in moments by looking at the local copies saved in your drive directory; and once again save that list in  a .out json file. Now it has a list of all the photos it can compare filenames also taking into account the date of the photo to produce a list of files to delete in a json file in the .out directory.
* delete-photos.py - Doesn't actually delete but move the files the previous script found into a directory you specify. Safer than just deleting, gives you a second chance to check them over and confirm the script didn't pick photos which should of been kept.

## How to Run?
    python3 find-photos-to-delete.py "USERNAME" "PASSWORD" "Local Path to Moments Directory"
    python3 delete-photos.py "Local Path to a folder to act as a recycle bin"

## How to run  the tests?
    python3 tests.py