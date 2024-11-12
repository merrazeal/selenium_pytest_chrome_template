import os
import shutil

import pytest

from core import settings


@pytest.fixture(scope="session", autouse=True)
def cleanup_downloads(request):
    directory_path = settings.DOWNLOADS_DIR

    yield

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path, ignore_errors=True)
