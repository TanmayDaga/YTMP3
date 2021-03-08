import pytube
import click


from pytube.cli import on_progress


@click.command()
@click.argument('url')
def ytd(url):
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(progressive=True)
    for a, b in enumerate(list(stream)):
        print(f'Press {a} for {b}')

    cho = int(input())
    stream[cho].download('/Users/tanmay06daga/Videos/'+stream[0].title+'.mp4')


if __name__ == '__main__':
    ytd()
