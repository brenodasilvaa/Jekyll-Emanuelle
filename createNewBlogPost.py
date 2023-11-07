from getInstagramPosts import GetNewInstagramPosts
from createMarkdown import GetNewPostMarkdown
import os

username = "emanuellecmaiola"
identifier = "seguiremos"
currentPath = os.getcwd()
postsPath = os.path.join(currentPath, "_posts")

posts = GetNewInstagramPosts(username, identifier)

for post in posts:

    postName = f'{post.date.year}-{post.date.month}-{post.date.day}-teste.md'

    postPath = os.path.join(postsPath, postName)

    if(os.path.exists(postPath)):
        continue

    postMd = GetNewPostMarkdown()
