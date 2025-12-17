# import markdown
import pdfkit

from utils.filename import generate_filename


# This might be removed
class GenerateDoc:
    def __init__(self, html):
        self.html = html
        self.pdf = None
        self.pdf_path = f"logs/summaries/{generate_filename()}.pdf"

        self.wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"

    def generate_pdf(self):
        try:
            config = pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf)
            self.pdf = pdfkit.from_string(
                self.html, output_path=None, configuration=config
            )

            with open(self.pdf_path, "wb") as f:
                f.write(self.pdf)

        except Exception as e:
            raise ValueError(f"something went wrong: {e}")
