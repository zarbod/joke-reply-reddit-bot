#!/usr/bin/python
import praw
import random

#Enter your correct Reddit information into the variable below

userAgent = 'PineappleBot'

cID = 'A7KoRHJgiGZlbA'

cSC= 'EdFZogndMrr10bK4gGNtJhEkRGqv-Q'

userN = 'Pineaaaapplebot'

userP ='Cougjbd3'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('bottesting')

bot_reply = ["Use the Force, Harry. \n- Gandalf"] #a list of possible replies
bot_reply.append("Ask not what you can do for your country, ask what your country can do for you. \n- Fohn J Kennedy")
bot_reply.append("The Big Boogie Monster will get you if you don't eat your lunch. \n- Albert Einstein")
bot_reply.append("Meesa Jar Jar Binks. Meesa think that you are stupid \n- Ben 10")
bot_reply.append("Conquer and Divide. \n- Winston Churchill")
bot_reply.append("72 percent of all statistics are made up. \n- FDR")
bot_reply.append("Slavery should be abolished as soon as possible. \n- Jefferson Davis")
bot_reply.append("I may not agree with what you say, but I will fight to the death to protect your right to say it. \n- Kim Jong Un")
bot_reply.append("I support Laissez-faire economics, and I will not tolerate the government intefering in our businesses \n- Karl Marx")
bot_reply.append("And when everyone's stupid, no one will be. \n- Mr. Incredible")
bot_reply.append("With great streaks, comes great desire to bullshit certain days just to keep up said streak. \n- Uncle Ben")


keywords = {'!quote', 'random quote', 'Bruh', 'quote'}  # a set of keywords to find in subreddits

id_list = []

for submission in subreddit.stream.comments(skip_existing=True):  # Checks every single comment in the stream.

    if id_list.count(submission.id) > 0:
        continue
    else:
        comment = submission.body.lower()  # makes the comment body lowercase so we can compare our keywords with it.

        for i in keywords:  # goes through our keywords
            if i in comment:
                numFound+=1
                print('Bot replying to: ')
                print("Title: ", submission.body)
                print("Score: ", submission.score)
                print("---------------------------------")
                print('Bot saying: ', "")
                print()
                index = random.randint(0,9)
                submission.reply(bot_reply[index])
                break

        id_list.append(submission.id)

        print(id_list)

if numFound == 0:
    print()
    print("Sorry, didn't find any comments with those keywords, try again!")