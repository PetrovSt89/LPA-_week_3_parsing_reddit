import datetime

from utils import add_vallue_to_dict, sorted_dict


def parsing(reddit, topic):

    authors_dict = {}
    comments_dict = {}
    three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)
    top_posts = reddit.subreddit(topic).new()

    for post in top_posts:
        date_created_subreddit = datetime.datetime.fromtimestamp(post.created_utc)

        if date_created_subreddit > three_days_ago:
            str_post_author = str(post.author)
            add_vallue_to_dict(str_post_author, authors_dict)
            comments_reddit = post.comments

            for comment in comments_reddit:
                str_comment_author = str(comment.author)
                add_vallue_to_dict(str_comment_author, comments_dict)

    sorted_authors_dict = sorted_dict(authors_dict)
    sorted_comments_dict =sorted_dict(comments_dict)

    return sorted_authors_dict, sorted_comments_dict