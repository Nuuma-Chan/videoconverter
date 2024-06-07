# FFmpeg Video to Audio Converter

This project provides a simple Python script to convert video files to audio files using FFmpeg. FFmpeg is a powerful multimedia framework that can decode, encode, transcode, mux, demux, stream, filter, and play almost anything that humans and machines have created.

## Features

- Convert video files to audio files
- Support for multiple audio formats (e.g., MP3, WAV, AAC)
- Easy to use and extend

## Requirements

- Python 3.x
- FFmpeg

## Installation

### Step 1: Install FFmpeg

FFmpeg needs to be installed on your system. You can download it from the [official FFmpeg website](https://ffmpeg.org/download.html).

For Windows, you can use the following command after downloading and extracting FFmpeg:

```sh
setx /M PATH "path\to\ffmpeg\bin;%PATH%"
