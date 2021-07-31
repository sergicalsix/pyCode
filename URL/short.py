from pyshorteners import Shortener
import sys

# passing instance
s = Shortener()
# Input
url = sys.argv[1]
#url = "https://qiita.com/e99h2121/items/9c2ca41df13e11bfc9ed"
tiny_url = s.tinyurl.short(url)
print(tiny_url)
#print(f"tiny_url: {tiny_url}")

