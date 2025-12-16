import subprocess
import re

from utils.filename import generate_filename

OUTPUT_FILE = f"logs/recordings/{generate_filename()}.wav"


class RecordingService:
    def __init__(self):
        self.device_number = None

    def set_device_number(self, device_name="BlackHole 2ch"):
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-list_devices",
            "true",
            "-f",
            "avfoundation",
            "-i",
            "dummy",
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        output = result.stderr

        for line in output.splitlines():
            if device_name in line:
                match = re.search(r"\[(\d+)\]", line)
                if match:
                    print("DEVICE NUMBER: ", int(match.group(1)))
                    self.device_number = int(match.group(1))

    def start(self):
        cmd = [
            "ffmpeg",
            "-f",
            "avfoundation",
            "-i",
            f":{self.device_number}",
            OUTPUT_FILE,
        ]  # change per OS

        print(f"started ffmpeg with cmd: {cmd}")
        return subprocess.Popen(
            cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
