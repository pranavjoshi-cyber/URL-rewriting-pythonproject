import pyshorteners
import numpy as np
import pyperclip

url = input("Enter the url to be shorten :")
def urlshortening(url):
    sh = pyshorteners.Shortener()
    print("The shortend url is ", sh.tinyurl.short(url))

urlshortening(url)