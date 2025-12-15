# This is for ffmpeg testing purposes, will be removed and is not part of the rest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import subprocess
import signal

YOUTUBE_URL = "https://www.youtube.com/watch?v=7vw445i8gOI"
OUTPUT_FILE = "logs/recordings/youtube_audio.wav"


def start_ffmpeg_recording():
    # ffmpeg -f avfoundation -i ":0" -t 15 sanity.wav
    cmd = ["ffmpeg", "-f", "avfoundation", "-i", ":0", OUTPUT_FILE]  # change per OS
    return subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


chrome_options = Options()
chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(YOUTUBE_URL)

    # Give the page time to load & start playback
    time.sleep(5)

    ffmpeg_proc = start_ffmpeg_recording()

    # Record for 20 seconds
    time.sleep(20)

finally:
    # Stop FFmpeg cleanly
    ffmpeg_proc.send_signal(signal.SIGINT)
    ffmpeg_proc.wait()

    driver.quit()

print("Recording saved to:", OUTPUT_FILE)
