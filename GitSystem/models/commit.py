class Commit:
    def __init__(self, message, files):
        self.message = message
        self.files = files.copy()

    def get_files(self):
        return self.files