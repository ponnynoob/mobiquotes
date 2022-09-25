import tweepy
import random
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

def main():

    window = tk.Tk()
    window.geometry('700x500')
    window.resizable(False, False)
    window.title("MobiQuotes")

    space1 = tk.Label(window, text="")
    space1.pack()

    img = ImageTk.PhotoImage(Image.open("logo.png"))
    panel = Label(window, image = img)
    panel.pack(side = "top", fill = "both", expand = "no")

    consumerKey = tk.Entry()
    consumerKey.insert(0, 'Consumer Key')
    consumerKey.pack(fill='x')

    consumerSecret = tk.Entry()
    consumerSecret.insert(0, 'Consumer Secret')
    consumerSecret.pack(fill='x')

    oauthToken = tk.Entry()
    oauthToken.insert(0, 'OAuth Token')
    oauthToken.pack(fill='x')

    oauthSecret = tk.Entry()
    oauthSecret.insert(0, 'OAuth Secret')
    oauthSecret.pack(fill='x')

    quote = Text(window, height = 13, width = 52)
    quote.config(highlightbackground="lightgrey", highlightthickness="1",font=("Helvetica", 14, "normal"))

    lines = open('quotes.txt').read().splitlines()
    text =random.choice(lines)

    quote.insert(tk.END, text)
    quote.pack(fill='x')

    def submit_name():
        twitter_auth_keys = {
            "consumer_key"        : consumerKey.get(),
            "consumer_secret"     : consumerSecret.get(),
            "access_token"        : oauthToken.get(),
            "access_token_secret" : oauthSecret.get()
        }

        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )
        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
        )
        api = tweepy.API(auth)
        tweet = quote.get("1.0",'end-1c')
        status = api.update_status(status=tweet)

        lines = open('quotes.txt').read().splitlines()
        text =random.choice(lines)
        quote.delete("1.0", tk.END)
        quote.insert(tk.END, " " + text)
        quote.pack(fill='x')

    submit= tk.Button(window, text= "Upload Quote",command=submit_name)
    submit.pack(pady=15, fill='x')

    window.mainloop()
 
if __name__ == "__main__":
    main()