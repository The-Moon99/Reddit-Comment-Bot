import praw
import random
import time

reddit = praw.Reddit(
    client_id="Client id",
    client_secret="client secret",
    user_agent="user agent"
username='username',
password='password')

subreddit = reddit.subreddit("")

hello_hello = ["hello world",
               "hello world",
               "hello world",
               "hello world"]

for submission in subreddit.hot(limit=20):
    print("********")
    print(submission.title)
    
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "hello" in comment_lower:
                print("**********")
                print(comment.body)
                random_index = random.randint(0,len(hello_hello)-1)
                comment.reply(hello_hello[random_index])
                time.sleep(0)
            
        
