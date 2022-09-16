#program that randomly generates a salty statement.

import random
def statement():
    a=random.randint(0,4)
    list_of_complaints = ["Why would you trust CS students to raise their hand??", 
    "When you speak, take a breath. It's like you're trying to beat the 14.1 syllables per second record", 
    "I've used GitLab but not GitHub before... Where'd y'all learn the latter??", 
    "If you had to write a program without bugs on the first shot, or die. I'd make you write C.",
    "The article was interesting...", "I wanted to cry during lab lmao. I didn't understand GitHub, but I left to avoid crying TvT."]
    print(list_of_complaints[a])

statement()