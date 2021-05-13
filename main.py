from pytube import YouTube
import moviepy.editor as mp
import re
import os


def convert(link, path):
    yt = YouTube(link)

    print('Download...')
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print('Download finished')

    print('File convert')
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')

            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    print('Convert Success!')


if __name__ == '__main__':
    link = str(input('Write a link YouTube for download: '))
    path = str(input('Write a path for save: '))
    convert(link, path)
