#!/usr/bin/env python3

import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HotReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        subprocess.call("make")
        return super().on_modified(event)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(HotReloadHandler(), "site", recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()
