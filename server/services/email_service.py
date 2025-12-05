from flask_mail import Mail, Message

MAIL_USERNAME = "edn.notes@gmail.com"
MAIL_PASSWORD = "wnmfvrrzrsotpldk"
MAIL_SERVER = "smtp.gmail.com"
MAIL_DEFAULT_SENDER = "edn.notes@gmail.com"


class EmailService:
    def __init__(self, app):
        app.config["MAIL_SERVER"] = MAIL_SERVER
        app.config["MAIL_PORT"] = 587
        app.config["MAIL_USE_TLS"] = True
        app.config["MAIL_USE_SSL"] = False
        app.config["MAIL_USERNAME"] = MAIL_USERNAME
        app.config["MAIL_DEFAULT_SENDER"] = MAIL_DEFAULT_SENDER
        app.config["MAIL_PASSWORD"] = MAIL_PASSWORD

        self.mail = Mail(app)

    def send(self, recipients, attachment):
        msg = Message(
            "Your edn meeting sumary",
            recipients=recipients,
            body="This is the generated meeting summary.",
        )

        # I assume sending only a pdf file
        msg.attach("summary.pdf", "application/pdf", attachment)
        self.mail.send(msg)
        return "Email sent successfully!"
