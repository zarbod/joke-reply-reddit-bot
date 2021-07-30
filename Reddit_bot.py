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

bot_reply = ["Use the Force, Harry. - Gandalf"] #a list of possible replies
bot_reply.append("Ask not what you can do for your country, ask what your country can do for you. - Fohn J Kennedy")
bot_reply.append("The Big Boogie Monster will get you if you don't eat your lunch. - Albert Einstein")
bot_reply.append("Meesa Jar Jar Binks. Meesa think that you are stupid - Ben 10")
bot_reply.append("Conquer and Divide. - Winston Churchill")
bot_reply.append("72 percent of all statistics are made up. - FDR")
bot_reply.append("Slavery should be abolished as soon as possible. - Jefferson Davis")
bot_reply.append("I may not agree with what you say, but I will fight to the death to protect your right to say it. - Kim Jong Un")
bot_reply.append("I support Laissez-faire economics, and I will not tolerate the government intefering in our businesses - Karl Marx")
bot_reply.append("And when everyone's stupid, no one will be. - Mr. Incredible")


keywords = {'!quote', 'random quote', 'Bruh'} #a set of keywords to find in subreddits

for submission in subreddit.stream.comments(): #Checks every single comment in the stream.

    comment = submission.body.lower() #makes the comment body lowercase so we can compare our keywords with it.

    for i in keywords: #goes through our keywords
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

if numFound == 0:
    print()
    print("Sorry, didn't find any comments with those keywords, try again!")