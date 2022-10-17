from pytube import YouTube
import os


def download(url, path):
    try:
        yt = YouTube(url)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        print(yt.title + ' successfully downloaded')
    except:
        print('Somenthing went wrong :(')


videos = ['https://www.youtube.com/watch?v=r8OipmKFDeM',
          'https://www.youtube.com/watch?v=8UVNT4wvIGY',
          'https://www.youtube.com/watch?v=oofSnsGkops']

for video in videos:
    download(video, '/home/luiza/Videos')
