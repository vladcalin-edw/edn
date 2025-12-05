import markdown
import pdfkit

import time


class GenerateDoc:
    def __init__(self, md_text):
        self.text = md_text
        self.extensions = ["extra", "codehilite", "toc"]
        self.title = None
        self.subtitle = None
        self.css = None

        self.html = ""
        self.pdf = None
        self.pdf_path = f"summaries/{time.time()}.pdf"

        self.wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"

    # Expects the data to be markdown
    def generate_html(self):
        html_body = markdown.markdown(
            self.text, extensions=self.extensions, output_format="html5"
        )

        css_block = f"<style>{self.css}</style>" if self.css else ""

        title_block = f"<h1>{self.title}</h1>" if self.title else ""
        subtitle_block = f"<h2>{self.subtitle}</h2>" if self.subtitle else ""

        self.html = f"""<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        {css_block}
        <title>{self.title or "Document"}</title>
        </head>
        <body>
        {title_block}
        {subtitle_block}
        {html_body}
        </body>
        </html>
        """

    def generate_pdf(self):
        # Generate html file from markdown
        # Move wkhtmltopdf to environments
        # Generate pdf name dynamically
        try:
            config = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf)
            self.pdf = pdfkit.from_string(
                self.html, output_path=None, configuration=config
            )

            with open(self.pdf_path, "wb") as f:
                f.write(self.pdf)

        except Exception as e:
            raise ValueError(f"something went wrong: {e}")

    def generate(self):
        self.generate_html()

        if not self.html:
            raise ValueError("html not created")

        self.generate_pdf()

        if not self.pdf:
            raise ValueError("pdf not created")
