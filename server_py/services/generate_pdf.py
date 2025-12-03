import markdown

import pdfkit
import os


def markdown_to_pdf(
    md_text,
    output,
    title=None,
    subtitle=None,
    css=None,
    extensions=None,
):
    if extensions is None:
        extensions = ["extra", "codehilite", "toc"]

    html_body = markdown.markdown(md_text, extensions=extensions, output_format="html5")

    css_block = f"<style>{css}</style>" if css else ""
    title_block = f"<h1>{title}</h1>" if title else ""
    subtitle_block = f"<h2>{subtitle}</h2>" if subtitle else ""

    html = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    {css_block}
    <title>{title or "Document"}</title>
    </head>
    <body>
    {title_block}
    {subtitle_block}
    {html_body}
    </body>
    </html>
    """

    config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")
    pdfkit.from_string(html, "summaries/hello.pdf", configuration=config)

    # 4️⃣  Convert HTML → PDF
    # xhtml2pdf works with a file‑like object; we use a BytesIO to keep it in memory.
    # with open(output, "wb") as out_f:
    #     # pisa.CreatePDF returns an object with .err that is False if success
    #     pisa_status = pisa.CreatePDF(
    #         src=html,
    #         dest=out_f,
    #         encoding="utf-8",
    #     )

    # return not pisa_status.err
