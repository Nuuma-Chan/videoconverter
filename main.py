#!/usr/bin/env python3

import sys
import os
import time
from moviepy.editor import VideoFileClip

def video_to_audio(fileName):
    try:
        # Extract filename and extension
        file, file_extension = os.path.splitext(fileName)
        
        # Create VideoFileClip object
        video_clip = VideoFileClip(fileName)
        
        # Set audio file name
        audio_file = file + ".mp3"
        
        # Convert video to audio
        video_clip.audio.write_audiofile(audio_file)
        
        print("Successfully converted", fileName, "into audio!")
    except Exception as e:
        print("An error occurred during conversion:", e)
        exit(1)

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 video_to_audio.py FileName')
        exit(1)
    
    filePath = sys.argv[1]
    
    # Check if the specified file exists
    if not os.path.exists(filePath):
        print("File not found!")
        exit(1)
        #this is nmc comment
    
    # Convert video to audio
    video_to_audio(filePath)
    time.sleep(1)

if __name__ == '__main__':
    main()
