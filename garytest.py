import praw, pprint

reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                    client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                    user_agent="validdit page checker")

submission = reddit.submission(url='https://www.reddit.com/r/news/comments/gxqkji/washington_dc_expects_citys_largest_protest_since/')
all_comments = submission.comments.list()

#news sources from https://blog.feedspot.com/usa_news_websites/ and https://blog.feedspot.com/canadian_news_websites/
#30 news sources listed
news_sources = ["cnn.com", "nytimes.com", "huffpost.com", "foxnews.com", "usatoday.com", 
                "reuters.com", "politico.com", "yahoo.com", "npr.org", "latimes.com",
                "brietbart.com", "nypost.com", "nbcnews.com", "abcnews.go.com", "cbsnews.com",
                "cbc.ca", "theglobeandmail.com", "ctvnews.ca", "globalnews.ca", "thestar.com",
                "huffingtonpost.ca", "nationalpost.com", "torontosun.com", "financialpost.com", "vancouversun.com",
                "macleans.ca", "montrealgazette.com", "citynews.ca", "metronews.ca", "calgaryherald.com"]

comments_with_links = []

for i in range(len(all_comments)):
    a = i
    cur_comment = vars(all_comments[i])["body_html"]
    start_of_link = 0 
    end_of_link = 0
    pointer = 0
    
    while pointer < len(cur_comment):
        try:
            cur_comment.index("<a href", pointer)
        except ValueError:
            start_of_link = 0
            end_of_link = 0
        else:
            start_of_link = cur_comment.index("<a href", pointer) + 9
            end_of_link = cur_comment.index("\">", pointer) - 1
            print(cur_comment[start_of_link:end_of_link])
            break
            # for i in range(len(news_sources)):
            #     if(cur_comment.index)
        



print(a)