from . import GenerateData, GenerateDoc, EmailService


class SummarizeService:
    def __init__(self, data, app, recipients):
        self.data = data
        self.app = app
        self.recipients = recipients

    def generate(self):
        try:
            # Generate summary
            generate_data = GenerateData()
            generate_data.build_prompt(self.data)
            generate_data.prompt_snapshot()
            generate_data.create_summary()
            generate_data.summary_snapshot()

            if not generate_data.response:
                raise ValueError("summary not created")

            # Make summary pdf
            generate_doc = GenerateDoc(html=generate_data.response)
            generate_doc.generate_pdf()

            if not generate_doc.html:
                raise ValueError("html missing")

            generate_doc.generate_pdf()

            if not generate_doc.pdf:
                raise ValueError("pdf missing")

            with self.app.app_context():
                email_service = EmailService(self.app)
                email_service.send(self.recipients, generate_doc.pdf)

            return generate_data.response

        except Exception as e:
            return f"something went wrong: {e}"
