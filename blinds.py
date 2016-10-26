import os

FILENAME="status"

class Blinds(object):
    """docstring for Blinds."""

    def read_last_status(self):
        saved_file=open(FILENAME, "r")
        if (saved_file.readline() == "True"):
            return True
        return False

    def write_last_status(self):
        saved_file=open(FILENAME, "w")
        if(self.blinds_open):
            saved_file.write('True')
        else:
            saved_file.write('False')
        saved_file.close()

    def open_blinds(self):
        if not self.blinds_open:
            self.blinds_open = True
            self.write_last_status()

    def close_blinds(self):
        if self.blinds_open:
            self.blinds_open = False
            self.write_last_status()

    def toggle_blinds(self):
        if self.blinds_open:
            self.close_blinds()
        else:
            self.open_blinds()
        return self.blinds_open

    def __init__(self):
        super(Blinds, self).__init__()
        self.blinds_open = self.read_last_status()
