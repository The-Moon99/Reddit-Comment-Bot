import praw
import random
import time

reddit = praw.Reddit(
    client_id="Client id",
    client_secret="client secret",
    user_agent="user agent",
username='username',
password='password')

subreddit = reddit.subreddit("Subreddit") # Subreddit thats going to be used.

hello_hello = ["hello world", # The word(s) or sentences that will be randomly chosen.
               "hello world",
               "hello world",
               "hello world"]

for submission in subreddit.hot(limit=20): # Choose between sorting of posts: besst hot new top or rising. limit=20 means it only looks to the first 20 posts
    print("********")
    print(submission.title)
    
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "hello" in comment_lower: # if the word 'hello' is in the comment it will comment one of the random words.
                print("**********")
                print(comment.body)
                random_index = random.randint(0,len(hello_hello)-1)
                comment.reply(hello_hello[random_index])
                time.sleep(0) # cooldown time.
            
        