import threading

from flask import Flask, request

from services import EmailService, SummarizeService


app = Flask(__name__)


# For dev purposes
# @app.route("/mail", methods=["POST"])
# def handle_mail():

#     pdf_file = None

#     with app.open_resource("summaries/1764829519.2568572.pdf") as pdf:
#         pdf_file = pdf.read()

#     if not pdf_file:
#         return "pdf missing"

#     email_service = EmailService(app)
#     email_service.send(["calinvladth@icloud.com"], pdf_file)

#     return "ok"


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
