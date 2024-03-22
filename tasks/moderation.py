from ai_devs_lib import AIDevsTasks, read_credentials
from openai import OpenAI

class Task(AIDevsTasks):
    def __init__(self, debug: bool = False):
        super().__init__("moderation", debug)

    def solve(self) -> dict:
        task = self.task()
        client = OpenAI(
            # This is the default and can be omitted
            api_key=self.creds['openai-api-key'],
        )

        response = client.moderations.create(
            input=task['input'],
            model='text-moderation-stable',
        )
        answer = [ int(r.flagged) for r in response.results ]

        return self.send_answer(dict(answer=answer))
