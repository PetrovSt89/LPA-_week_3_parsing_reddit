import praw

from logic import parsing
from utils import print_dict


def main():

    TOPIC = "python"

    reddit = praw.Reddit(
        client_id="kvxS8qp-wiyR8bWV1zVwfg",
        client_secret="gnYaImh5X5NR17UD1_7IWW7TqYQN9w",
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) \
      AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
      )
    
    sorted_authors_dict, sorted_comments_dict =  parsing(reddit, TOPIC)

    print(f'Топ авторов постов за 3 дня по теме {TOPIC}:')
    print_dict(sorted_authors_dict)
    print(f'Топ авторов комментариев за 3 дня по теме {TOPIC}:')
    print_dict(sorted_comments_dict)


if __name__ == "__main__":
    main()