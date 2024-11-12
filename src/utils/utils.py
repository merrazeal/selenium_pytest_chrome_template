
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from core import settings


def is_file_downloaded(
    directory_path: str,
    handler: FileSystemEventHandler,
    timeout=settings.WEB_WAITER_DOWNLOAD_TIMEOUT,
) -> bool:
    observer = Observer()
    observer.schedule(handler, directory_path, recursive=False)
    observer.start()

    try:
        if handler.event.wait(timeout):
            return True
        raise TimeoutError("Timed out waiting for file downloaded")
    finally:
        observer.stop()
