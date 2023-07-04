import pyshorteners

urls = pyshorteners.Shortener()

print("Enter URL to shorten")
url = input()


newURl = urls.tinyurl.short(url)
print(newURl)
