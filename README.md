# Reddit Image Scraper 🖼️

## Overview 📜
This project is a Python script that scrapes images from specified subreddits using Reddit's API. Perfect for gathering inspiration or exploring different topics through images!

## Setup ⚙️

1. **Install Python and Pip 🐍**.
   - Make sure you have Python installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).
   - Pip is the package installer for Python and usually comes with Python. If not, you can install it by following [this guide](https://pip.pypa.io/en/stable/installation/).

2. **Clone this repository ⬇️**.
   - Run the following command in your terminal to clone the repository:
   
     ```bash
     git clone https://github.com/yourusername/reddit-image-scraper.git
     ```

3. **Navigate to the project directory 📂** and install dependencies:
   - After cloning, navigate to the project folder:
   
     ```bash
     cd reddit-image-scraper
     ```

   - Then install the required packages by running:

     ```bash
     pip install -r requirements.txt
     ```

4. **Create a `.env` file with your Reddit API credentials 🔐**.
   - You’ll need to sign up for a Reddit API account. Follow [this guide](https://github.com/reddit-archive/reddit/wiki/OAuth2) to get your `client_id`, `client_secret`, `user_agent`, and fill them into a `.env` file like so:

     ```
     CLIENT_ID=your_client_id
     CLIENT_SECRET=your_client_secret
     USER_AGENT=your_user_agent
     ```

## Usage 🚀

1. **Populate `sub_list.csv` with the subreddits you want to scrape 📝**.
   - Open the `sub_list.csv` file and add the subreddits you want to scrape, one per line.
   - Example:
   
     ```
     cats
     EarthPorn
     Art
     ```

2. **Run the script by entering:**

   ```bash
   python scraper.py
