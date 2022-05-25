import os
from pathlib import Path
import csv
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, 'market','.env'))

SECRET_KEY = os.environ.get('SECRET_KEY',default='django-insecure-493s(bzyk&n22(0st%mj&zikk7j@fta*wu)pl3yyr!j8ih$emw')

CORS_ORIGINS_WHITELIST = os.environ.get('CORS_ORIGINS_WHITELIST') 

print(CORS_ORIGINS_WHITELIST)

