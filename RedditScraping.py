import argparse
import requests
from os import getenv
from dotenv import load_dotenv
import praw

#set up the parser
parser = argparse.ArgumentParser()
#add the arguments
parser.add_argument("--link")

#parse the arguments
args = parser.parse_args()

load_dotenv(dotenv_path='./key.env')

reddit = praw.Reddit(
    client_id = getenv("client_id"),
    client_secret = getenv("secret_key"),
    user_agent = "WTFRIT",
    
)

for submission in reddit.subreddit("rit").hot(limit=10):
    print(submission.selftext)
