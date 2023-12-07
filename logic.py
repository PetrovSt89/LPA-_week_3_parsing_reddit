import collections
import datetime


def parsing(reddit, topic):

    authors_dict = collections.defaultdict(int)
    comments_dict = collections.defaultdict(int)
    three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)
    top_posts = reddit.subreddit(topic).new()

    for post in top_posts:
        date_created_subreddit = datetime.datetime.fromtimestamp(post.created_utc)

        if date_created_subreddit > three_days_ago:
            str_post_author = str(post.author)
            authors_dict[str_post_author] += 1
            comments_reddit = post.comments

            for comment in comments_reddit:
                str_comment_author = str(comment.author)
                comments_dict[str_comment_author] += 1

    sorted_authors_dict = sorted(authors_dict.items(), key=lambda x: -x[1])
    sorted_comments_dict =sorted(comments_dict.items(), key=lambda x: -x[1])

    return sorted_authors_dict, sorted_comments_dict

if __name__ == '__main__':
    print('привет')