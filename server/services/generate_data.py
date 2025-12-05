import ollama


class GenerateData:
    def __init__(self):
        self.prompt = ""
        self.response = ""

    def build_prompt(self, data):
        self.prompt = f"""
        Summarize the following meeting transcript in 3 - 8 phrases and only return the summary.
        Generate a list of action items and only return the action items.

        Transcript JSON:
        {data}

        Return Markdown.
        """

    def create_summary(self):
        if not self.prompt:
            raise ValueError("prompt is missing")

        result = ollama.generate(model="llama3", prompt=self.prompt)

        if not result["response"]:
            raise ValueError("response not generated")

        self.response = result["response"]
