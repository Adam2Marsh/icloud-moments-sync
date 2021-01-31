class Utilities:
    
    def checkForFile(self, filename):
        try:
            with open(filename) as f:
                return True
        except IOError:
            return False
                