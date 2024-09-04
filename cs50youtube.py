import yt_dlp
from art import *
from Color_Console import ctext
import datetime
import os

# Functions
def get_info(yt_url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(yt_url, download=False)
    return info

def length(yt_url):
    info = get_info(yt_url)
    duration = info.get('duration')
    return str(datetime.timedelta(seconds=duration))

def author(yt_url):
    info = get_info(yt_url)
    return info.get('uploader')

def title(yt_url):
    info = get_info(yt_url)
    return info.get('title')

def resolutions(yt):
    formats = yt['formats']
    resolutions = [f"{format['height']}p" for format in formats if 'height' in format and format['vcodec'] != 'none']
    return list(set(resolutions))

def streams(yt):
    return yt['formats']

def on_progress(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes') or d.get('filesize')
        bytes_downloaded = d.get('downloaded_bytes')
        percentage_of_completion = (bytes_downloaded / total_size) * 100 if total_size else 0
        totalsz = (total_size / 1024) / 1024 if total_size else 'Unknown'
        remain = ((total_size - bytes_downloaded) / 1024) / 1024 if total_size else 'Unknown'
        dwnd = (bytes_downloaded / 1024) / 1024
        percentage_of_completion = round(percentage_of_completion, 2)
        print(f'\rDownload Progress: {percentage_of_completion}%, Total Size: {totalsz:.2f} MB, Downloaded: {dwnd:.2f} MB, Remaining: {remain:.2f} MB', end='', flush=True)

def main():
    # Credentials & Title
    from art import text2art
    Art = text2art("CS50 Youtube", font="larry3d")
    ctext(Art, "red", "black")
    ctext('=' * 120, "blue", "black")
    ctext("Mohamed Yasser's CS50 Project | Linkedin:www.linkedin.com/in/mykhalifa", "white", "red")
    ctext('=' * 120, "blue", "black")
    ctext("Inspired By: Ahmed Osama | FB:www.facebook.com/ahmed.osama.572", "white", "green")
    ctext('=' * 120, "blue", "black")

    # Prompt URL
    while True:
        try:
            link = input("Please Enter Video URL: ")
            ydl_opts = {
                'format': 'bestaudio/best',
                'progress_hooks': [on_progress],
                'verbose': False,
                'quiet': True,
                'no_warnings': True,
                'noprogress': True
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                yt_info = ydl.extract_info(link, download=False)
        except Exception as e:
            ctext(f"URL is Not Correct. Error: {str(e)}", "red", "black")
        else:
            break

    # Show Video Data
    ctext('=' * 120, "blue", "black")
    print("Video Name: ", end="")
    ctext(title(yt_info), "green", "black")
    print("Video Length: ", end="")
    ctext(length(yt_info), "green", "black")
    print("Video Author: ", end="")
    ctext(author(yt_info), "green", "black")
    ctext('=' * 120, "blue", "black")

    # Show Video Resolutions
    print("Available Resolutions: ", end="")
    resolutionsList = resolutions(yt_info)
    ctext(" | ".join(resolutionsList), "green", "black")
    ctext('=' * 120, "blue", "black")

    # Prompt Resolution
    while True:
        try:
            res = input("Choose a Quality [ex: 720p]: ").strip()
            available_res = [f for f in streams(yt_info) if 'height' in f and f"{f['height']}p" == res]
            if not available_res:
                raise ValueError("Not Valid Value")
        except Exception as e:
            ctext(f"Please Choose a Quality From the list Above 👆. Error: {str(e)}", "red", "black")
        else:
            choose = next((f for f in available_res if f.get('filesize')), available_res[0])
            break

    # Error Handling for Missing Format
    if choose is None:
        ctext(f"Error: Unable to find a suitable format for resolution {res}. Please try a different resolution.", "red", "black")
    else:
        # Show Video Size
        print("Video Size: ", end='')
        filesize_mb = round(choose.get('filesize', 0) / 1024 / 1024, 1) if choose.get('filesize') else 'Unknown'
        ctext(f"{filesize_mb} MB", "green", "black")
        ctext('=' * 120, "blue", "black")

        # Prompt If Agree On Download?
        ch = input("Are you sure to Download? [Y / N] ").upper()

        #download_path
        if os.name == 'nt':  # Windows
            download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        else:  # macOS/Linux
            download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

        #download
        if ch == "Y":
            try:
                ydl_opts = {
                    'format': f"{choose['format_id']}+bestaudio",
                    'progress_hooks': [on_progress],
                    'merge_output_format': 'mp4',
                    'verbose': False,
                    'quiet': True,
                    'no_warnings': True,
                    'noprogress': True,
                    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                ctext("\nDownloaded Successfully!", "green", "black")
                ctext("Thanks For Using Downloader 💘❤", "white", "blue")
            except Exception as e:
                ctext(f"Failed to Download 💥👎. Error: {str(e)}", "red", "black")
        else:
            ctext("Thanks For Using Downloader 💘❤", "white", "blue")

    # Pause Console
    input()

if __name__ == "__main__":
    main()
