import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')



DOWNLOADS_DIR = os.path.join(os.path.dirname(__file__), 'downloads')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
