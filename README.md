## Overview
I developed these 2 scripts to remove pictures from Synology moments which had been synced via the app but deleted from iCloud. The 2 scripts do the following:
* find-photos-to-delete.py - This one will connect to the iCloud API and grab a list of all your photos, then save that as a json file in the .out directory. It will then read all the photos in moments by looking at the local copies saved in your drive directory; and once again save that list in  a .out json file. Now it has a list of all the photos it can compare filenames also taking into account the date of the photo to produce a list of files to delete in a json file in the .out directory.
* delete-photos.py - Doesn't actually delete but move the files the previous script found into a directory you specify. Safer than just deleting, gives you a second chance to check them over and confirm the script didn't pick photos which should of been kept.

## How to Run?
1. First you need to grab a release version and download the files:
```
wget https://github.com/Adam2Marsh/icloud-moments-sync/archive/1.0.0.tar.gz
```

2. Then you can untar the scripts:
```
tar -xvf 1.0.0.tar.gz 
```

3. Now enter the directory with the scripts:
```
cd icloud-moments-sync-1.0.0
```

4. Now you can run the first script:
python3 find-photos-to-delete.py "USERNAME" "PASSWORD" "Local Path to Moments Directory"
```
python3 find-photos-to-delete.py example@icloud.com password /var/services/homes/username/Drive/Moments/Mobile/phoneName
```

5. Once happy you can then run the second script:
python3 delete-photos.py "Local Path to a folder to act as a recycle bin"
```
python3 delete-photos.py ./recycle_bin
```


## Extra Information on each Scripts
```
python3 find-photos-to-delete.py  -h
usage: find-photos-to-delete.py [-h] [-ri] [-rl] icloud_email icloud_password local_directory

Compares your icloud photos with a local copy like moments

positional arguments:
  icloud_email          Email address used when logging into iCloud
  icloud_password       Password used when logging into iCloud
  local_directory       Directory which contains local copy of pictures

optional arguments:
  -h, --help            show this help message and exit
  -ri, --refresh_icloud
                        Force a refresh of icloud photos
  -rl, --refresh_local  Force a refresh of local photos
```
```
python3 delete-photos.py -h
usage: delete-photos.py [-h] recycle_bin

Removes files from moments but moving files found in find-photos-to-delete.py

positional arguments:
  recycle_bin  Path to directory to move files to

optional arguments:
  -h, --help   show this help message and exit
```

## How to run  the tests?
    python3 tests.py