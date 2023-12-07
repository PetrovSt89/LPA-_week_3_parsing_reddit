import os
from dataclasses import dataclass


@dataclass
class Config:
    client_id: str
    client_secret: str
    user_agent: str


def load():
    return Config(
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        user_agent=os.environ['USER_AGENT']
    )


config = load()

