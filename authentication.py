import os
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

login = os.getenv("moex_user")
password = os.getenv("moex_password")

auth_headers = {"Authorization": f"Basic {login}:{password}"}
