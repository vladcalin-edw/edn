from datetime import datetime


def generate_filename():
    now = datetime.now()
    return now.strftime("%Y-%m-%d-%H:%M:%S")
