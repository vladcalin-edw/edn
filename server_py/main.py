from flask import Flask, request

import ollama
from services import generate_pdf


MODEL_NAME = "llama3"
JSON_FORMAT = {"summary": "", "action_items": ""}

app = Flask(__name__)


# BETTER HANDLING FOR PROMPT
def build_prompt(data):
    prompt = f"""
    Summarize the following meeting transcript in 3 - 5 phrases.
    Generate a list of action items.

    Give me just the summary and action items, no other text.

    Transcript JSON:
    {data}

    Return Markdown.
    """
    return prompt


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    prompt = build_prompt(data)

    result = ollama.generate(model="llama3", prompt=prompt)

    md = result["response"]

    generate_pdf.markdown_to_pdf(md, "/summaries/test.pdf")

    return "ok"


if __name__ == "__main__":
    # For production you’d probably want a WSGI server (gunicorn, uWSGI, …)
    app.run(host="0.0.0.0", port=8000, debug=True)
