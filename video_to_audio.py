import subprocess
import os
import sys

def convert_video_to_audio_ffmpeg(video_file, k, output_ext="mp3"):
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"audio/aud"+str(k)+".mp3"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)

if __name__ == "__main__":

    path_of_the_directory = 'videos'
    print("Files and directories in a specified path:")
    k=0
    for filename in os.listdir(path_of_the_directory):
        k=k+1
        f = os.path.join(path_of_the_directory, filename)
        if os.path.isfile(f):
            convert_video_to_audio_ffmpeg(f, k)
    # vf = sys.argv[1]
    # convert_video_to_audio_ffmpeg(vf)