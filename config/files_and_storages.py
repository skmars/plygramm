import os
from enum import Enum

from config.env import BASE_DIR, env, env_to_enum


class FileUploadStrategy(Enum):
    STANDARD = "standard"
    DIRECT = "direct"


class FileUploadStorage(Enum):
    LOCAL = "local"
    # cloud_storage = cloud_storage e.g. 's3'


FILE_UPLOAD_STRATEGY = env_to_enum(
    FileUploadStrategy, env("FILE_UPLOAD_STRATEGY")  # default="standard"
)
FILE_UPLOAD_STORAGE = env_to_enum(FileUploadStorage, env("FILE_UPLOAD_STORAGE"))  # default="local"

FILE_MAX_SIZE = env.int("FILE_MAX_SIZE")  # default=10485760 - 10 MiB

if FILE_UPLOAD_STORAGE == FileUploadStorage.LOCAL:
    MEDIA_ROOT_NAME = "media"
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
    MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"
