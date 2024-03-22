from ai_devs_lib import AIDevsTasks

class Task(AIDevsTasks):
    def __init__(self, debug: bool = False):
        super().__init__("helloapi", debug)

    def solve(self) -> dict:
        cookie = self.task()['cookie']
        return self.send_answer(dict(answer=cookie))