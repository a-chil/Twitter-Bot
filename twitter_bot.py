import tweepy
from time import sleep
from tkinter import *

# Twitter Dev account authorization keys:
auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

# Creating the GUI
root = Tk()
root.title('Twitter API app')
root.configure(background='#00acee')
root.geometry('500x500')

# Labels and entries for each of listed functions:

search_label = Label(root, text="Search")
search_entry = Entry(root)
search_label.configure(background='#00acee')
search_entry.configure(background='#00acee')
search_label.pack()
search_entry.pack()

amount_label = Label(root, text="Number of tweets")
amount_entry = Entry(root)
amount_label.configure(background='#00acee')
amount_entry.configure(background='#00acee')
amount_label.pack()
amount_entry.pack()

fav_label = Label(root, text="Favorite?")
fav_entry = Entry(root)
fav_label.configure(background='#00acee')
fav_entry.configure(background='#00acee')
fav_label.pack()
fav_entry.pack()

rt_label = Label(root, text="Retweet?")
rt_entry = Entry(root)
rt_label.configure(background='#00acee')
rt_entry.configure(background='#00acee')
rt_label.pack()
rt_entry.pack()

reply_label = Label(root, text="Reply?")
reply_entry = Entry(root)
reply_label.configure(background='#00acee')
reply_entry.configure(background='#00acee')
reply_label.pack()
reply_entry.pack()

response_label = Label(root, text="Response:")
response_entry = Entry(root)
response_label.configure(background='#00acee')
response_entry.configure(background='#00acee')
response_label.pack()
response_entry.pack()


# Main function which interacts with API and Tweepy library to perform actions on twitter
def main():
    search = search_entry.get()
    amt = int(amount_entry.get())
    fav = fav_entry.get()
    rt = rt_entry.get()
    reply = reply_entry.get()
    response = response_entry.get()

    if fav == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(amt):
            try:
                tweet.favorite()
                print("fav success")
            except tweepy.TweepError as e:
                print(e.reason)

    if rt == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(amt):
            try:
                tweet.retweet()
                print("rt success")
            except tweepy.TweepError as e:
                print(e.reason)

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(amt):
            try:
                print("\ntweet by @" + tweet.user.screen_name)
                api.update_status("@" + tweet.user.screen_name +
                                  ' ' + response, in_reply_to_status_id=tweet.user.id)
            except tweepy.TweepError as e:
                print(e.reason)


submit = Button(root, text="Submit", command=main)
submit.pack()

root.mainloop()
