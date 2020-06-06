import praw

reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                        client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                        user_agent="validdit page checker")
newsSubreddit = reddit.subreddit("news")

print(reddit.read_only)

for submission in newsSubreddit.hot(limit = 10):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
    print()

