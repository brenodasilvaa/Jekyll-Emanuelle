import instaloader
import datetime
from typing import List

def GetNewInstagramPosts(instaProfile:str, identifier:str) -> List[instaloader.Post]:
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, instaProfile)
    posts = profile.get_posts()
    listPosts = List[instaloader.Post]

    for val in posts:
        if (datetime.datetime.now() - val.date).days < 1 and identifier in val.caption:
            listPosts.append(val)
    
    return listPosts

