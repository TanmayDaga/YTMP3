import pytube
from pytube.cli import on_progress
import moviepy.editor as mp
import os
import click
import io


def video_downloader(url):
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams
    if stream.filter(file_extension='mp3'):
        file = stream.filter(file_extension='mp3').first()
        file.download(
            "/Users/tanmay06daga/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/" + file.title + ".mp3")
        return None, None, True
    else:
        stream = yt.streams.filter(progressive=True)

        with io.BytesIO() as buffer:
            path = stream[0].download(stream[0].stream_to_buffer(buffer))
            print(path)

        return path, stream[0].title, False


@click.command()
@click.argument('url')
def ytmp3(url):
    print('Downloading video...')
    path, title, boolo = video_downloader(url)
    print('Converting video to mp3')
    if not boolo:
        file = mp.VideoFileClip(path)
        file.audio.write_audiofile(
            "/Users/tanmay06daga/Music/Music/Media.localized/Music/Unknown Artist/Unknown Album/" + title + ".mp3")

        #     Deleting video file
        print("Deleting file")
        os.remove(path)
    print("File Downloaded")


if __name__ == '__main__':
    ytmp3()
