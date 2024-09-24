# app/settings.py

import os
from dotenv import load_dotenv


class Settings:
    DATABASE_URL: str

    def __init__(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv("DATABASE_URL")

        if self.DATABASE_URL is None:
            raise ValueError("DATABASE_URL environment variable is not set!")


# Create a single instance of the Settings
settings = Settings()
