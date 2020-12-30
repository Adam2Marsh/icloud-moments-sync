import unittest

from MomentPhotos import MomentPhoto
from iCloudPhotos import iCloudPhoto

class TestMomentPhoto(unittest.TestCase):
    def test_return_returnPath(self):
        photo = MomentPhoto("/Volumes/home/Drive/Moments/Mobile/Martins Banana Tree/2017-12-08/IMG_0006.MOV")
        self.assertEqual(photo.returnPathDate(), "2017-12-08")

    def test_returnName(self):
        photo = MomentPhoto("/Volumes/home/Drive/Moments/Mobile/Martins Banana Tree/2017-12-08/IMG_0006.MOV")
        self.assertEqual(photo.returnName(), "IMG_0006")

    def test_returnFileName(self):
        photo = MomentPhoto("/Volumes/home/Drive/Moments/Mobile/Martins Banana Tree/2017-12-08/IMG_0006.MOV")
        self.assertEqual(photo.returnFileName(), "IMG_0006.MOV")

    def test_returnPath(self):
        photo = MomentPhoto("/Volumes/home/Drive/Moments/Mobile/Martins Banana Tree/2017-12-08/IMG_0006.MOV")
        self.assertEqual(photo.returnPath(), "/Volumes/home/Drive/Moments/Mobile/Martins Banana Tree/2017-12-08/IMG_0006.MOV")

    def test_returnNameWithDate(self):
        photo = MomentPhoto("/Volumes/home/Drive/Moments/Mobile/Martins Banana Tree/2017-12-08/IMG_0006.MOV")
        self.assertEqual(photo.returnNameWithDate(), "2017-12-08/IMG_0006")

class TestiCloudPhoto(unittest.TestCase):
    def test_returnFilename(self):
        photo = iCloudPhoto("IMG_0010.JPG", "2017-12-08T22:55:19.557000+00:00")
        self.assertEqual(photo.returnFilename(), "IMG_0010.JPG")

    def test_returnName(self):
        photo = iCloudPhoto("IMG_0010.JPG", "2017-12-08T22:55:19.557000+00:00")
        self.assertEqual(photo.returnName(), "IMG_0010")

    def test_returnDate(self):
        photo = iCloudPhoto("IMG_0010.JPG", "2017-12-08T22:55:19.557000+00:00")
        self.assertEqual(photo.returnDate(), "2017-12-08")

if __name__ == '__main__':
    unittest.main()