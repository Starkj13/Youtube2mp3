from pytube import YouTube

print("Download one or many")
print("1: One")
print("2: From text file")
chose = input()

def Download(url):
   try:
       video = YouTube(url)
       stream = video.streams.filter(only_audio=True).first()
       stream.download(filename=f"{video.title}.mp3")
       print("The video " + video.title + " downloaded in MP3")
   except KeyError:
     print("Unable to fetch video information. Please check the video URL or your network connection.")

if(chose == '1'):
    print("Input Yt link")
    url = input()
    Download(url)
    
if(chose == '2'):
 with open('videos.txt', 'r') as file:
    urls = []
    for url in file:
        url = url.strip()
        urls.append(url)
    for url in urls:
        Download(url)

