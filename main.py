import pytube

# TODO: Convert 3gpp to mp3 or mp4
# TODO: Download a playlist
try:
    video_url = 'https://www.youtube.com/watch?v=pT68FS3YbQ4'
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download('/home/luiza/Videos')
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")
