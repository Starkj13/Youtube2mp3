import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
import eyed3

# constanst
output_dir = "mp4_output" 
output_dir_mp3 = "mp3_output"

os.makedirs(output_dir_mp3, exist_ok=True)

# Function to download a YouTube video as an MP4 file
def download_youtube_video(url, output_dir):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=output_dir)
    return os.path.join(output_dir, f"{yt.title}.mp4")

# Function to convert MP4 to MP3
def convert_mp4_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    mp3_file_path = os.path.join(output_dir_mp3, os.path.basename(mp3_file))
    video.audio.write_audiofile(mp3_file_path)

# Function to process YouTube URLs from the terminal input
def process_youtube_urls_from_terminal(output_dir):
    urls = []
    while True:
        print("Enter a YouTube URL (or 'done' to finish):")
        url = input()
        if url.lower() == 'done':
            break
        urls.append(url)

    for url in urls:
        mp4_file = download_youtube_video(url, output_dir)
        if mp4_file:
            mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
            convert_mp4_to_mp3(mp4_file, mp3_file)
            print(f"Downloaded {mp4_file}, converted to {mp3_file}, and added metadata.")

# Function to process YouTube URLs from a text file
def process_youtube_urls_from_file(file_path, output_dir):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        mp4_file = download_youtube_video(url, output_dir)
        if mp4_file:
            mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
            convert_mp4_to_mp3(mp4_file, mp3_file)
            print(f"Downloaded {mp4_file}, converted to {mp3_file}, and added metadata.")

if __name__ == "__main__":
    choice = input("Choose input method ('file' or 'input'): ").lower()

    if choice == 'file':
        input_file = "videos.txt"
        process_youtube_urls_from_file(input_file, output_dir)
    elif choice == 'input':
        process_youtube_urls_from_terminal(output_dir)
    else:
        print("Invalid input method. Please choose 'file' or 'input'.")
