import praw
from dotenv import load_dotenv
import os

def create_reddit_instance():
    # Load environment variables
    load_dotenv()

    # Set up PRAW with credentials from .env file
    return praw.Reddit(
            client_id = os.getenv("ZAGz-tAWTZlqijUKyVjnMw"),
client_secret = os.getenv("x4M2wUIG7r1wi7qDA-_kuIXobyU5jg"),
user_agent = os.getenv("reddit_image_scraper by u/Ambitious-Street-516"),
username = os.getenv("u/Ambitious-Street-516"),
password = os.getenv("@poorvS1ngh"),
    )
