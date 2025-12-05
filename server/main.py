from flask import Flask, request

from services import GenerateDoc, GenerateData, EmailService


app = Flask(__name__)


# For dev purposes
@app.route("/mail", methods=["POST"])
def handle_mail():

    pdf_file = None

    with app.open_resource("summaries/1764829519.2568572.pdf") as pdf:
        pdf_file = pdf.read()

    if not pdf_file:
        return "pdf missing"

    email_service = EmailService(app)
    email_service.send(["calinvladth@icloud.com"], pdf_file)

    return "ok"


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if not data:
        return "data missing"

    # Enable threading for this
    try:
        # Generate summary
        generate_data = GenerateData()
        generate_data.build_prompt(data)
        generate_data.create_summary()

        if not generate_data.response:
            return "summary not created"

        # Make summary pdf
        generate_doc = GenerateDoc(md_text=generate_data.response)
        generate_doc.generate_html()

        if not generate_doc.html:
            return "html missing"

        generate_doc.generate_pdf()

        if not generate_doc.pdf:
            return "pdf missing"

        return generate_data.response

    except Exception as e:
        return f"something went wrong: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
