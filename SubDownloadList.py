import praw
import requests
import os
import cv2
import numpy as np
from dotenv import load_dotenv

# Load environment variables for Reddit API credentials
load_dotenv()
client_id = os.getenv("ZAGz-tAWTZlqijUKyVjnMw")
client_secret = os.getenv("x4M2wUIG7r1wi7qDA-_kuIXobyU5jg")
user_agent = os.getenv("reddit_image_scraper by u/Ambitious-Street-516")
username = os.getenv("u/Ambitious-Street-516")
password = os.getenv("@poorvS1ngh")

# Initialize PRAW with credentials
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

POST_SEARCH_AMOUNT = 5  # Number of posts to search

# Function to create a directory if it doesn't exist
def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Directories for saving and ignoring images
image_dir = "images"
ignore_dir = "ignore_images"
create_folder(image_dir)
create_folder(ignore_dir)

# Function to download and save image
def download_image(url, filepath):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image from {url}")

# Function to check if image should be ignored
def should_ignore_image(image_path, ignore_dir):
    image = cv2.imread(image_path)
    for ignore_file in os.listdir(ignore_dir):
        ignore_image = cv2.imread(os.path.join(ignore_dir, ignore_file))
        if np.array_equal(image, ignore_image):
            return True
    return False

# Main function to scrape images
def scrape_subreddits():
    with open("sub_list.csv", "r") as file:
        subreddits = file.read().splitlines()

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        print(f"Scraping subreddit: {subreddit_name}")

        for submission in subreddit.hot(limit=POST_SEARCH_AMOUNT):
            if submission.url.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(image_dir, f"{submission.id}.jpg")
                if not os.path.exists(image_path):
                    download_image(submission.url, image_path)

                    if should_ignore_image(image_path, ignore_dir):
                        print(f"Ignoring and deleting downloaded image: {image_path}")
                        os.remove(image_path)

scrape_subreddits()
