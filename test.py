import praw

def getRedditClient():
    reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                     client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                        user_agent="validdit page checker")
    submission = reddit.submission(id="gx8t25")
    print(submission.author)
    print(submission.title)
    print(submission.score)
    print(submission.upvote_ratio)
    print(submission.url)
    print(submission.subreddit)
    print(submission.num_comments)
    #only gets the top level comments - ones without parent comments, the starter of the comment chain.
    for comment in submission.comments:
        print(comment.body)

getRedditClient()