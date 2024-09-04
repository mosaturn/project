# CS50 YouTube
#### Video Demo:  https://youtu.be/yXoaUBOK9tA
#### Description: A simple YouTube Video Downloader
# YouTube Video and Audio Downloader

## Features

- Customizable Video Quality: Choose your preferred video quality from a filtered list based on resolution and format (mp4).
- Forced Audio Codec: The audio codec is forced to use ID 233 for consistency.
- Automatic Merging: The script downloads the video and audio separately and merges them using ffmpeg.

## Prerequisites

- Python 3.x
- yt-dlp library
- ffmpeg (Make sure ffmpeg is installed and accessible from the command line)

## Installation

1. Clone this repository:
   git clone https://github.com/mosaturn/project.git

2. Navigate to the project directory:
   cd your-repo-name

3. Install the required Python packages:
   pip install -r requirements.txt

4. Install ffmpeg:
   - **Windows**: Download and install from ffmpeg.org.
   - **macOS**: Install via Homebrew:
     brew install ffmpeg
   - **Linux**: Install via package manager:
     sudo apt-get install ffmpeg

## Usage

1. Run the script:
   python cs50youtube.py

2. Paste the YouTube URL when prompted.

3. Choose your desired video quality from the list provided.

4. The script will download the video and audio, then merge them into a single file.

## Example

python cs50youtube.py

- **URL Prompt**: Enter the YouTube URL.
- **Quality Prompt**: Choose the desired video quality (e.g., 720p).

The merged video will be saved in the default download location.

## Troubleshooting

- Merging Error: If you see an error related to merging, ensure ffmpeg is installed correctly and is in your system's PATH.

## License

This project is licensed under the MIT License.
