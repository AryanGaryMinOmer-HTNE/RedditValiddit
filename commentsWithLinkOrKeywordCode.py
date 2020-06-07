import praw, pprint

reddit = praw.Reddit(client_id="MuFZGhJium139Q",
                    client_secret="JCGwE1FgXThG1DYlHZnEcwj1WN4",
                    user_agent="validdit page checker")

submission = reddit.submission(url='https://www.reddit.com/r/news/comments/gxqkji/washington_dc_expects_citys_largest_protest_since/')
all_comments = list(submission.comments)

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

comments_with_links = [] # holds the comments, links, start and end index of link, and karma
comments_with_keywords = [] # holds the comments, keyword found, start and end index of link, and karma

# loop going through every comment
for i in range(len(all_comments)):
    try:
        cur_comment = vars(all_comments[i])["body_html"]
    except KeyError:
        cur_comment = ""
    else:
        cur_comment = vars(all_comments[i])["body_html"]

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
                
                comments_with_links.append([clean_body, cur_comment[start_of_link:end_of_link], start_of_link, end_of_link, vars(all_comments[i])["score"]])
    
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
            clean_body = clean_body.translate({ord('['): None})
            clean_body = clean_body.translate({ord(']'): None})
            clean_body = clean_body.replace("(" + cur_comment[start_of_link:end_of_link] + ")", "")
            clean_body = clean_body.replace('\n', ' ')
            comments_with_keywords.append([clean_body, keywords[j], start_of_word, end_of_word, vars(all_comments[i])["score"]])



        