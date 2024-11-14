from dotenv import load_dotenv # Required to get shit from the .env file
from atproto import Client # 'pip install atproto' to install
import os # Required to make dotenv work
load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
VIDEO_PATH = os.getenv('VIDEO_PATH')


glungus = Client() # You can replace "glungus" with anything you want
glungus.login(USERNAME, PASSWORD) # Authentication

with open (VIDEO_PATH, 'rb') as blob:
    glungus_video = blob.read() # Reads video data

glungus.send_video(text='', video=glungus_video) # Posts glungus :3

# Credit: https://atproto.blue/en/latest/atproto_client/index.html, Tam for giving me the atproto.blue doc and https://docs.bsky.app/docs/tutorials/creating-a-post
