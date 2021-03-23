import pytube
import click

from pytube.cli import on_progress


@click.command()
@click.argument('url')
@click.argument('path')
def ytd(url, path):
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(progressive=True)
    stream.first().download(path+'/' + stream.first().title + '.mp4')


if __name__ == '__main__':
    ytd()
