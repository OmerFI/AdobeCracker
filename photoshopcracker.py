from shutil import move
from os import getenv, rmdir
from os.path import isfile, isdir
from random import choices

path_to_current_file = r"C:\Program Files\Adobe\Adobe Photoshop CC 2018\AMT\application.xml"
path_to_temp_new_destination = getenv("TEMP") + r"\application.xml"
path_to_new_destination = r"C:\Program Files\Adobe\Adobe Photoshop CC 2018\AMT\application.xml"


class Cracker():
    def __init__(self):
        self.checkoutanddel()
        self.moveit()
        self.crackit()
        self.placeit()

    @staticmethod
    def checkoutanddel():
        if isfile(path_to_temp_new_destination):
            move(path_to_temp_new_destination, path_to_current_file)

        if isdir(path_to_temp_new_destination):
            rmdir(path_to_temp_new_destination)

    @staticmethod
    def moveit():
        move(path_to_current_file, path_to_temp_new_destination)

    @staticmethod
    def createnumber():
        numbers = list("1234567890")
        numberwithspace = choices(numbers, k=5)
        numberstr = ""
        for i in numberwithspace:
            numberstr += i
        return numberstr

    @classmethod
    def crackit(cls):
        with open(path_to_temp_new_destination, "r") as f:
            file = f.read()

        numberstr = cls.createnumber()
        file = file[:1271] + numberstr + file[1276:]

        with open(path_to_temp_new_destination, "w") as f:
            f.write(file)

    @staticmethod
    def placeit():
        move(path_to_temp_new_destination, path_to_new_destination)


if __name__ == '__main__':
    cracker = Cracker()
