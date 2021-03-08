import moviepy.editor as mp
import click
import os

@click.command()
@click.argument('path')
def vmp3(path):
    clip = mp.VideoFileClip(path)
    clip.audio.write_audiofile('/Users/tanmay06daga/Music/Music/Media.localized/Music/'+os.path.splitext(os.path.basename(path))[0]+'.mp3')

if __name__ == '__main__':
    vmp3()