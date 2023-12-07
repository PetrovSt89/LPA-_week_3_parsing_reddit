import praw

from config import client_id, client_secret, user_agent
from logic import parsing
from utils import print_dict


def main():

    TOPIC = "python"

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
      )
    
    sorted_authors_dict, sorted_comments_dict =  parsing(reddit, TOPIC)

    print(f'Топ авторов постов за 3 дня по теме {TOPIC}:')
    print_dict(sorted_authors_dict)
    print(f'Топ авторов комментариев за 3 дня по теме {TOPIC}:')
    print_dict(sorted_comments_dict)


if __name__ == "__main__":
    main()