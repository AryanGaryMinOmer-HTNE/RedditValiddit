import praw

def getRedditClient():
    redditLink = "https://www.reddit.com/r/Jokes/comments/gxmqa6/mens_help_line_letter_of_the_month/"
    redditPost = praw.models.Submission.id_from_url(redditLink)
    print(praw.models.Submission.id_from_url(redditLink))
    
    reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                        client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                        user_agent="validdit page checker")
    submission = reddit.submission(id=redditPost)
    print(submission.title)
    #print(vars(submission))
    
    author = submission.author
    print(author.name)
    print(author.comment_karma)
    print(author.link_karma)
    print(author.has_verified_email)

    subreddit = submission.subreddit
    print("r/"+subreddit.display_name)
    print(subreddit.quarantine)
    
    print(submission.title)
    print(submission.score)
    downvoteNum = (1-submission.upvote_ratio)
    print(round(downvoteNum*submission.score))
    if(submission.url != redditLink): url = submission.url
    print(url)
    print(submission.num_comments)
    #only gets the top level comments - ones without parent comments, the starter of the comment chain.
    #for comment in submission.comments:
    #   print(comment.body)

getRedditClient()