import ollama


# MODEL = "llama3"
MODEL = "gpt-oss:20b"


class GenerateData:
    def __init__(self):
        self.prompt = ""
        self.response = ""

    def build_prompt(self, data):
        self.prompt = f"""
        Meeting Report Template

        Please provide the following information in the format below:

        Title: [Insert title of meeting]
        Date: [Insert date in the format: December 5, 2025]
        Duration: [Insert duration of meeting]
        Attendees: [Insert names of attendees]

        Meeting Summary: [Insert summary of meeting (1-2 paragraphs)]

        Key Takeaways: [Insert key takeaway 1] [Insert key takeaway 2] *

        Action Items: [Insert person X's action item]: [Insert action item], due by [Insert due date (if any)] [Insert person Y's action item]: [Insert action item], due by [Insert due date (if any)] *…

        Topics: Topic 1: [Insert description of topic 1] [Bullet point for topic 1] *… Topic 2: [Insert description of topic 2] [Bullet point for topic 2] *… Topic 3: [Insert description of topic 3] [Bullet point for topic 3] *…

        Transcript: {data}

        Next Steps: Person 1: [Insert next step 1] Person 2: [Insert next step 2] *…

        You can paste your meeting transcript in the Transcript section, and I will return the formatted text with markdown.

        Please note that you should format the transcript as follows:
        ```
        **Meeting Purpose**
        Text of the meeting purpose

        **Meeting Summary**
        Text of the meeting summary

        **Key Takeaways**
        * Idea 1
        * Idea 2
        *

        **Action Items**
        * Person X: Item 1, due by [Date]
        * Person Y: Item 2, due by [Date]
        *…

        **Topics**
        Topic 1: Text of topic 1
        * Bullet point for topic 1

        Topic 2: Text of topic 2
        * Bullet point for topic 2

        Topic 3: Text of topic 3
        * Bullet point for topic 3

        ``` 
        """

    def create_summary(self):
        if not self.prompt:
            raise ValueError("prompt is missing")

        result = ollama.generate(model=MODEL, prompt=self.prompt)

        if not result["response"]:
            raise ValueError("response not generated")

        self.response = result["response"]
