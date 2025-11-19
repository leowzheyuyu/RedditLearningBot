# RedditLearningBot
## 🤖 Overview
This is a small-scale, non-commercial Python project using the PRAW library.

The primary goal is for the developer (bisbisness88) to learn the fundamentals of connecting to the Reddit API, handling OAuth authentication, and performing basic data manipulation.

## ✨ Intended Functionality
The bot will perform a single, simple action:
1. **Access:** Connect to the Reddit API once every 24 hours.
2. **Read:** Fetch the top 5 highest-scoring posts from a designated testing subreddit (initially r/MyTestBotLab).
3. **Post:** Create a summary post in the same testing subreddit containing the titles and links of those 5 posts.

The bot will **not** operate in any major public subreddits without explicit moderator permission and is strictly contained to low-volume, scheduled tasks.

## 📍 Intended Subreddit(s)
* **Primary:** `r/MyTestBotLab` (A private, developer-owned subreddit for testing.)
* **Future (Conditional):** `r/learnprogramming` (Only after successful, long-term testing and direct permission from the moderator team.)

## 💻 Tech Stack
* **Language:** Python
* **Library:** PRAW (Python Reddit API Wrapper)
* **Hosting:** Local machine/Self-hosted (for testing phase)
