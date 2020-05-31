# imported modules
import os
import shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# set current working directory to Downloads folder
os.chdir('C:\\Users\\jjgar\\Downloads')

# directories to each folder in Downloads
pdfdir = 'C:\\Users\\jjgar\\Downloads\\PDF\'s'
imgdir = 'C:\\Users\\jjgar\\Downloads\\Images'
exedir = 'C:\\Users\\jjgar\\Downloads\\EXE\'s'
miscdir = 'C:\\Users\\jjgar\\Downloads\\Misc'

# TODO: if directories don't exist, create them
# if not os.path.exists(pdfdir):
#     os.makedirs('PDF\'s')
#     os.makedirs('Images')
#     os.makedirs('EXE\'s')
#     os.makedirs('Misc')


# class for file handling
class FileHandler(FileSystemEventHandler):
    # when Downloads folder is modified
    def on_modified(self, event):
        # get a list of current files in directory
        items = os.listdir()

        # create lists for file name and extensions
        filenames = []
        filexts = []

        # remove pdfs, imgs, exes, and misc out of list
        items.remove("PDF's")
        items.remove("EXE's")
        items.remove("Misc")
        items.remove("Images")

        # splits filenames and file extensions into seperate lists
        for x in range(len(items)):
            filename, fileexts = os.path.splitext(items[x])
            filenames.append(filename)
            filexts.append(fileexts)

        # splits each file type into different lists
        for x in range(len(items)):
            if filexts[x] == '.pdf':
                shutil.move(items[x], pdfdir)

            elif filexts[x] == '.jpg' or filexts[x] == '.png' or filexts[x] == '.jpeg':
                shutil.move(items[x], imgdir)

            elif filexts[x] == '.exe':
                shutil.move(items[x], exedir)

            elif filexts[x] == '':
                shutil.move(items[x], miscdir)


# path to Downloads folder
path = 'C:\\Users\\jjgar\\Downloads'

# create an object of FileHandler class
event_handler = FileHandler()

# create an object of Observer class
observer = Observer()

# schedule observer object recursively and starts
observer.schedule(event_handler, path, recursive=True)
observer.start()

# will run every second until KeyboardInterrupt
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
