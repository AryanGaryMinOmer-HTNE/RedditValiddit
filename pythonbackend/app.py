from flask import Flask, render_template, request
import praw 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/search', methods=['POST'])
def getRedditClient():
    redditlink = request.form['link']
    redditID = praw.models.Submission.id_from_url(redditlink)
    reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                        client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                        user_agent="validdit page checker")
    submission = reddit.submission(id=redditID)
    return render_template('search.html', titl=submission.title, auth=submission.author, up=submission.ups, dow=submission.downs)


    #hello