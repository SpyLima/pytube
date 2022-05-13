from pytube import YouTube
import subprocess
import requests

url = input(str("url: "))
yt = YouTube(url)

th = yt.thumbnail_url
th_out = requests.get(th, stream=True)

header = """
\t • TITLE = {}
\t • VIEWS = {}
\t • AUTHOR ={}
\t • PUBLISH IN = {}
\t • DESCRIPTION = \n \n {} \n
"""

print(header.format(yt.title, yt.views, yt.author, yt.publish_date, yt.description))

if th_out.status_code == 200:
    subprocess.run(["/usr/bin/kitty", "icat"], input=th_out.content)
else:
    print('\tcannot print the url')
