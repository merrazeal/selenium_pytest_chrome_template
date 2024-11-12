import os
import threading
from watchdog.events import FileSystemEvent, FileSystemEventHandler


class PartialDownloadHandler(FileSystemEventHandler):
    def __init__(self, startswith_file_path: str):
        self.event = threading.Event()
        self.startswith_file_path = startswith_file_path

    def on_modified(self, event: FileSystemEvent) -> None:
        file_name = os.path.basename(event.src_path)
        if file_name.startswith(self.startswith_file_path):
            self.event.set()
