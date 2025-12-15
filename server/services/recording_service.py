import subprocess
from utils.filename import generate_filename

OUTPUT_FILE = f"logs/recordings/{generate_filename()}.wav"


class RecordingService:
    def __init__(self):
        pass

    def start(self):
        cmd = ["ffmpeg", "-f", "avfoundation", "-i", ":0", OUTPUT_FILE]  # change per OS

        print(f"started ffmpeg with cmd: {cmd}")
        return subprocess.Popen(
            cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
