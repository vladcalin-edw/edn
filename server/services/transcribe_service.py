import whisper
import json


class TranscribeService:
    def __init__(self, audio_file):
        self.model = whisper.load_model("large")
        self.audio_file = audio_file
        self.result = None

    def speech_to_text(self):
        print("transcript generating")
        self.result = self.model.transcribe(f"logs/recordings/{self.audio_file}")

        print("transcript created")
        self.write_text_file()
        self.wite_json_file()

    def write_text_file(self):
        with open(
            f"logs/transcriptions/{self.audio_file}.txt", "w", encoding="utf-8"
        ) as f:
            f.write(self.result["text"])

    def wite_json_file(self):
        # Build JSON with start, end, and text
        segments = self.result.get("segments", [])
        json_data = [
            {
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"].strip(),
            }
            for segment in segments
        ]

        with open(f"logs/transcriptions/{self.audio_file}.json", "w") as f:
            json.dump(json_data, f, indent=4)
