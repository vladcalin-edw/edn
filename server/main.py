from flask import Flask, request

from services import GenerateDoc, GenerateData


app = Flask(__name__)


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

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
        generate_doc.generate_pdf()

        print(generate_doc.pdf)

        return generate_data.response

    except Exception as e:
        return f"something went wrong: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
