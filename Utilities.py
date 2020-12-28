class Utilities:
    
    def checkForFile(self, filename):
        try:
            with open(filename) as f:
                return False
        except IOError:
            return True