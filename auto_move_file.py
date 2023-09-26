import sys
import time
import random

import shutil
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/vimimutalik/Downloads"
to_dir = "/Applications/Coding Classes/Python/Homework Projects/H103"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Some one deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Hey, some one modified {event.src_path}")

    def on_moved(self, event):
        print(f"Hey, someone moved {event.src_path}")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()