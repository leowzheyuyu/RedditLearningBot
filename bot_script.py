# bot_script.py
import praw
import os

# --- Bot Initialization ---
def initialize_reddit_bot():
    """Initializes the PRAW Reddit instance."""
    try:
        reddit = praw.Reddit(
            client_id=os.environ.get("REDDIT_CLIENT_ID"),
            client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
            user_agent="MyFirstRedditBot v0.1 by u/BeBeSan11 (Learning Project)",
        )
        print("Reddit instance initialized successfully.")
        return reddit
    except Exception as e:
        print(f"Error initializing PRAW: {e}")
        return None

# --- Main Bot Logic ---
def run_bot():
    """Contains the main logic for the bot's operation."""
    reddit = initialize_reddit_bot()

    if not reddit:
        return

    # Replace with actual testing subreddit name
    TEST_SUBREDDIT = "MyTestBotLab" 
    
    print(f"Fetching top 5 posts from r/{TEST_SUBREDDIT}...")
    
    # This section is currently commented out to prevent execution errors
    """
    try:
        subreddit = reddit.subreddit(TEST_SUBREDDIT)
        
        summary_text = "Today's Top 5 Posts:\n\n"
        
        for i, submission in enumerate(subreddit.top(limit=5)):
            summary_text += f"{i+1}. **{submission.title}** ([Link]({submission.url}))\n"
            
        print("Summary generated successfully.")
        # Post the summary to the subreddit (Uncomment when ready to test)
        # subreddit.submit(title="Daily Top Posts Summary", selftext=summary_text)

    except Exception as e:
        print(f"An error occurred during bot operation: {e}")
    """
    
if __name__ == "__main__":
    run_bot()
