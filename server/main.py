import threading

from flask import Flask, request, render_template

from services import SummarizeService, MeetingBot, RecordingService, TranscribeService


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/meeting", methods=["POST"])
def meeting():
    data = request.get_json()
    meeting_url = data["meeting_url"]
    if not meeting_url:
        return "meeting url missing"

    if not "teams.microsoft.com" in meeting_url:
        return "only works with microsoft teams at the moment"

    meeting_bot = MeetingBot(meeting_url=meeting_url)

    meeting_bot_thread = threading.Thread(
        target=meeting_bot.access_meeting, name="access_meeting"
    )

    meeting_bot_thread.start()
    return "the meeting bot started"


@app.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.get_json()
    if not data:
        return "data missing"

    if not data["audio_file"]:
        return "recipients missing"

    transcribe_service = TranscribeService(data["audio_file"])

    transcribe_service_thread = threading.Thread(
        target=transcribe_service.speech_to_text, name="generate_transcript"
    )

    transcribe_service_thread.start()

    return "the transcript is generating"


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if not data:
        return "data missing"

    if not data["recipients"]:
        return "recipients missing"

    if not data["meeting"]:
        return "meeting missing"

    summarize_service = SummarizeService(
        data=data["meeting"],
        app=app,
        recipients=data["recipients"],
    )

    summarize_service_thread = threading.Thread(
        target=summarize_service.generate, name="generate_summary"
    )

    summarize_service_thread.start()

    return "the summary is generating"


if __name__ == "__main__":
    recording_service = RecordingService()
    recording_service.set_device_number()
    app.run(host="0.0.0.0", port=8000, debug=True)
