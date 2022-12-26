import os
from google.cloud import storage

os.environment["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/credentials.json"

storage_client = storage.Client()

dir(storage_client)
