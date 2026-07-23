from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("URJA_BASE_URL")
USERNAME = os.getenv("URJA_USERNAME")
PASSWORD = os.getenv("URJA_PASSWORD")