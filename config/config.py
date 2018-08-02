import os

class Config:
    def __init__(self):
        self.gmail_pw = self.getEnvVar('GMAIL_PW')

    def getEnvVar(self, key):
        if key in os.environ:
            return os.environ[key]
        return None

config = Config()
