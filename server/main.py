import threading

from flask import Flask, request, render_template

from services import SummarizeService


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# @app.route("/test", methods=["POST"])
# def test():
#     data = request.get_json()

#     if not data:
#         return "data missing"

#     if not data["recipients"]:
#         return "recipients missing"

#     if not data["meeting"]:
#         return "meeting missing"

#     print("data: ", data)
#     return "raw_emails"


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
    app.run(host="0.0.0.0", port=8000, debug=True)
