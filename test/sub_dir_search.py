import os

def search(dirname):
    try:
        filename = os.lisdir(dirname)
    except PermissionError:
        pass

    search("C:/")