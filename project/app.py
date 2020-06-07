from flask import Flask, render_template, request
from json import dumps
import praw 

app = Flask(__name__)

#news sources from https://blog.feedspot.com/usa_news_websites/ and https://blog.feedspot.com/canadian_news_websites/
#30 news sources listed + reddit
news_sources = ["cnn.com", "nytimes.com", "huffpost.com", "foxnews.com", "usatoday.com", 
                "reuters.com", "politico.com", "yahoo.com", "npr.org", "latimes.com",
                "brietbart.com", "nypost.com", "nbcnews.com", "abcnews.go.com", "cbsnews.com",
                "cbc.ca", "theglobeandmail.com", "ctvnews.ca", "globalnews.ca", "thestar.com",
                "huffingtonpost.ca", "nationalpost.com", "torontosun.com", "financialpost.com", "vancouversun.com",
                "macleans.ca", "montrealgazette.com", "citynews.ca", "metronews.ca", "calgaryherald.com",
                "reddit.com"]
keywords = ["fake", "accurate", "biased", "radical", "politic", "made-up", "corrupt", "racist"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/search', methods=['POST'])
def getRedditClient():
    redditlink = request.form['link']
    redditID = praw.models.Submission.id_from_url(redditlink)
    reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                        client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                        user_agent="validdit page checker")
    submission = reddit.submission(id=redditID)
    
    comments_with_links = [] # holds the comments, links, start and end index of link, and karma
    comments_with_keywords = [] # holds the comments, keyword found, start and end index of link, and karma
    all_comments = list(submission.comments)

    # loop going through every comment
    for i in range(len(all_comments)):
        try:
            cur_comment = vars(all_comments[i])["body_html"]
        except KeyError:
            cur_comment = ""
        else:
            cur_comment = vars(all_comments[i])["body_html"]

        link_dup = False
        keyword_dup = False
        start_of_link = 0 
        end_of_link = 0
        start_of_word = 0
        end_of_word = 0
        pointer = 0

        # try/catch for locating comments with article/reddit links
        try:
            cur_comment.index("<a href", pointer)
        except ValueError:
            start_of_link = 0
            end_of_link = 0
        else:
            start_of_link = cur_comment.index("<a href=\"", pointer) + 9
            end_of_link = cur_comment.index("\">", start_of_link)
            for j in range(len(news_sources)):
                if(news_sources[j] in cur_comment[start_of_link:end_of_link]):

                    clean_body = vars(all_comments[i])["body"]
                    clean_body = clean_body.translate({ord('['): None})
                    clean_body = clean_body.translate({ord(']'): None})
                    clean_body = clean_body.replace("(" + cur_comment[start_of_link:end_of_link] + ")", "")
                    clean_body = clean_body.replace('\n', ' ')
                    
                    for k in range(len(comments_with_links)):
                        if(comments_with_links[k][0] == clean_body):
                            link_dup = True

                    if(link_dup == False):
                        comments_with_links.append([clean_body, cur_comment[start_of_link:end_of_link], vars(all_comments[i])["score"]])
        
        # try/catch for locating comments containing key words
        for j in range(len(keywords)):
            try:
                cur_comment.index(keywords[j])
            except ValueError:
                start_of_word = 0
                end_of_word = 0
            else:
                start_of_word = cur_comment.index(keywords[j])
                end_of_word = start_of_word + len(keywords[j])

                clean_body = vars(all_comments[i])["body"]
                clean_body = clean_body.replace("(" + cur_comment[start_of_link:end_of_link] + ")", "")
                for k in range(len(keywords)):
                    if(keywords[k] in clean_body):
                        clean_body = clean_body.translate({ord('['): None})
                        clean_body = clean_body.translate({ord(']'): None})
                        clean_body = clean_body.replace('\n', ' ')

                        for k in range(len(comments_with_keywords)):
                            if(comments_with_keywords[k][0] == clean_body):
                                keyword_dup = True

                        if(keyword_dup == False):
                            comments_with_keywords.append([clean_body, keywords[j], vars(all_comments[i])["score"]])

    author = submission.author
    url = "No Linked URL"
    if(submission.url != redditlink): url = submission.url

    # returns info that will be displayed to user 
    return render_template('search.html', 
                            titl=submission.title, 
                            auth=author, 
                            score=submission.score, 
                            ratio=submission.upvote_ratio,
                            url=url,
                            authCommentKarm=author.comment_karma,
                            authLinkKarm=author.link_karma,
                            authVerified=author.has_verified_email,
                            comNum=submission.num_comments,
                            comWithLink=comments_with_links,
                            comWithKey=comments_with_keywords)

if __name__== "__main__":
    app.run()
