from pathlib import Path

class MomentPhoto:
    
    def __init__(path, name):
        self.path = path
        self.name = name

    def returnName(self):
        return self.name
    
    def returnPath(self):
        return self.path

    def returnFileSizeInBytes(self):
        return Path(self.returnPath).stat().st_size