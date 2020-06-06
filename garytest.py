import praw

reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                        client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                        user_agent="validdit page checker")

print(reddit.read_only)

for submission in reddit.subreddit("news").hot(limit = 10):
    print(submission.title)

